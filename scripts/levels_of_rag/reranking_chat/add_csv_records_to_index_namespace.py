import csv
from pinecone import Pinecone
import os
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import time
import uuid
from langchain_text_splitters import TokenTextSplitter
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

load_dotenv()

api_key = os.getenv("PINECONE_API_KEY")
index_name = os.getenv("PINECONE_ALL_MINILM_L6_V2_INDEX")
custom_namespace='chat_with_txt'
pc = Pinecone(api_key=api_key)
index = pc.Index(index_name)

print("BEFORE", index.describe_index_stats())

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2', device='cpu')

# Initialize the token text splitter
text_splitter = TokenTextSplitter(
    chunk_size=250,
    chunk_overlap=125,
    encoding_name="cl100k_base"  # Default encoding for most tokenizers
)

# Thread-safe counter for progress tracking
processed_count = 0
lock = threading.Lock()

def process_chunk(chunk_data, total_chunks):
    """Process a single chunk and upload to Pinecone"""
    global processed_count
    
    chunk_id, chunk = chunk_data
    
    # Create embedding for the chunk
    embedding = model.encode([chunk])[0]
    
    # Upsert to Pinecone
    index.upsert(
        vectors=[
            {
                "id": str(uuid.uuid4()),
                "values": embedding,
                "metadata": {
                    "chunk_id": int(chunk_id),
                    "content": chunk,
                    "total_chunks": total_chunks,
                    "created_at": int(time.time() * 1000)
                },
            }
        ],
        namespace=custom_namespace,
    )
    
    # Update progress counter
    with lock:
        global processed_count
        processed_count += 1
        print(f"Processed chunk {processed_count}/{total_chunks}")
    
    return chunk_id

# Read and chunk the text file
with open("./data/levels_of_rag/chat_with_txt/the_boston_cooking_school_cookbook.txt", "r", encoding="utf-8") as kb_file:
    text_content = kb_file.read()
    
# Split the text into chunks
chunks = text_splitter.split_text(text_content)
total_chunks = len(chunks)
print(f"Created {total_chunks} chunks from the text file")

# Process chunks in parallel with pauses every 100 chunks
max_workers = 10  # Number of parallel threads
batch_size = 100  # Process 100 chunks at a time

for batch_start in range(0, total_chunks, batch_size):
    batch_end = min(batch_start + batch_size, total_chunks)
    batch_chunks = list(enumerate(chunks[batch_start:batch_end], start=batch_start))
    
    print(f"Processing batch {batch_start//batch_size + 1}: chunks {batch_start+1}-{batch_end}")
    
    # Process this batch in parallel
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all chunks in this batch
        future_to_chunk = {executor.submit(process_chunk, chunk_data, total_chunks): chunk_data for chunk_data in batch_chunks}
        
        # Wait for all chunks in this batch to complete
        for future in as_completed(future_to_chunk):
            try:
                chunk_id = future.result()
            except Exception as exc:
                print(f'Chunk {future_to_chunk[future][0]} generated an exception: {exc}')
    
    # Pause between batches (except after the last batch)
    if batch_end < total_chunks:
        print(f"Pausing for 2 seconds before next batch...")
        time.sleep(2)

print('Record count AFTER adding knowledge ->', index.describe_index_stats())