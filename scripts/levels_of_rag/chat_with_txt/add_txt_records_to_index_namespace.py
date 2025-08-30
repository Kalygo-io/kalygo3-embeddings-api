import os
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import time
import uuid
import hashlib
import yaml
import tiktoken
from langchain_text_splitters import TokenTextSplitter
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
import re
from typing import List, Dict, Tuple, Any

load_dotenv()

api_key = os.getenv("PINECONE_API_KEY")
index_name = os.getenv("PINECONE_ALL_MINILM_L6_V2_INDEX")
custom_namespace = 'chat_with_txt'
pc = Pinecone(api_key=api_key)
index = pc.Index(index_name)

print("BEFORE", index.describe_index_stats())

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2', device='cpu')

# Initialize the token text splitter
text_splitter = TokenTextSplitter(
    chunk_size=200,
    chunk_overlap=50,
    encoding_name="cl100k_base"  # Default encoding for most tokenizers
)

# Thread-safe counter for progress tracking
processed_count = 0
lock = threading.Lock()

def parse_metadata_from_file(text_content: str) -> Tuple[Dict[str, Any], str]:
    """
    Parse YAML metadata from the top of a file and return both metadata and content without metadata.
    
    Expected format:
    - YAML metadata section at the top of the file
    - Metadata section is delimited by --- at the beginning and end
    - Example:
      ---
      video_title: "What is Ollama?"
      video_url: "https://www.youtube.com/watch/glkQIUTCAK4"
      tags:
        - tutorial
        - ollama
      ---
      
      Content starts here...
    
    Returns:
        Tuple of (metadata_dict, content_without_metadata)
    """
    metadata = {}
    lines = text_content.split('\n')
    content_lines = []
    
    # Check if file starts with YAML front matter (---)
    if lines and lines[0].strip() == '---':
        # Find the end of YAML section
        yaml_end_index = -1
        for i, line in enumerate(lines[1:], 1):
            if line.strip() == '---':
                yaml_end_index = i
                break
        
        if yaml_end_index > 0:
            # Extract YAML content
            yaml_content = '\n'.join(lines[1:yaml_end_index])
            
            try:
                # Parse YAML metadata
                metadata = yaml.safe_load(yaml_content) or {}
                
                # Convert all values to strings for consistency
                string_metadata = {}
                for key, value in metadata.items():
                    if isinstance(value, (list, dict)):
                        string_metadata[key] = str(value)
                    else:
                        string_metadata[key] = str(value) if value is not None else ""
                
                metadata = string_metadata
                
                # Content starts after the second ---
                content_lines = lines[yaml_end_index + 1:]
                
            except yaml.YAMLError as e:
                print(f"Warning: Failed to parse YAML metadata: {e}")
                # If YAML parsing fails, treat the whole file as content
                content_lines = lines
        else:
            # No closing --- found, treat as content
            content_lines = lines
    else:
        # No YAML front matter, treat as content
        content_lines = lines
    
    content_without_metadata = '\n'.join(content_lines)
    return metadata, content_without_metadata

def prepend_metadata_to_chunk(chunk: str, chunk_index: int, total_chunks: int, file_metadata: Dict[str, Any], filename: str) -> str:
    """
    Prepend YAML front matter metadata to a chunk with additional chunk-specific metadata.
    
    Args:
        chunk: The original chunk content
        chunk_index: The index of this chunk (0-based)
        total_chunks: Total number of chunks in the file
        file_metadata: Metadata from the original file's YAML front matter
        filename: The original filename
    
    Returns:
        Chunk with prepended metadata
    """
    # Create chunk-specific metadata
    chunk_metadata = {
        "chunk_number": f"{chunk_index + 1} of {total_chunks}",  # 1-based for readability
        "filename": filename,
        "upload_timestamp_in_unix": int(time.time())
    }
    
    # Combine file metadata with chunk metadata
    combined_metadata = {**file_metadata, **chunk_metadata}
    
    # Convert to YAML format
    yaml_content = yaml.dump(combined_metadata, default_flow_style=False, sort_keys=False)
    
    # Create the final chunk with YAML front matter
    final_chunk = f"---\n{yaml_content}---\n\n{chunk}"
    
    return final_chunk

def process_chunk(chunk_data, total_chunks, filename, file_metadata):
    """Process a single chunk and upload to Pinecone"""
    global processed_count
    
    chunk_id, chunk = chunk_data
    
    # Skip empty chunks
    if not chunk.strip():
        return chunk_id
    
    # Prepend metadata to chunk
    chunk_with_metadata = prepend_metadata_to_chunk(
        chunk, chunk_id, total_chunks, file_metadata, filename
    )
    
    # Create embedding for the chunk
    embedding = model.encode([chunk_with_metadata])[0]
    
    # Create unique ID for the vector
    vector_id = hashlib.sha256(f"{filename}_{chunk_id}_{chunk[:50]}".encode()).hexdigest()
    
    # Prepare metadata
    metadata = {
        "filename": filename,
        "chunk_id": chunk_id,
        "content": chunk_with_metadata,
        "chunk_size_tokens": len(chunk.split()),  # Approximate token count
        "upload_timestamp": str(int(time.time() * 1000)),
        "total_chunks": total_chunks
    }
    
    # Add file metadata if available
    if file_metadata:
        # Prefix file metadata keys to avoid conflicts
        for key, value in file_metadata.items():
            metadata[f"file_{key}"] = value
    
    # Add chunk-specific metadata
    metadata["chunk_number"] = chunk_id + 1
    
    # Upsert to Pinecone
    index.upsert(
        vectors=[
            {
                "id": vector_id,
                "values": embedding,
                "metadata": metadata,
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

# Read and process the text file
file_path = "./data/levels_of_rag/chat_with_txt/the_boston_cooking_school_cookbook.txt"
filename = os.path.basename(file_path)

# Validate file type
if not (filename.endswith('.txt') or filename.endswith('.md')):
    print(f"Error: Only .txt and .md files are supported. File '{filename}' is not supported.")
    exit(1)

with open(file_path, "r", encoding="utf-8") as kb_file:
    text_content = kb_file.read()

# Parse metadata from the file (only for .md files)
if filename.endswith('.md'):
    metadata, content_without_metadata = parse_metadata_from_file(text_content)
    
    # Log metadata if found
    if metadata:
        print(f"Found YAML front matter in {filename}:")
        for key, value in metadata.items():
            print(f"  {key}: {value}")
    else:
        print(f"No YAML front matter found in {filename}")
else:
    # For .txt files, use the content as-is without metadata parsing
    metadata = {}
    content_without_metadata = text_content
    print(f"Processing {filename} as plain text file (no metadata parsing)")

# Split the text into chunks
chunks = text_splitter.split_text(content_without_metadata)
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
        future_to_chunk = {
            executor.submit(process_chunk, chunk_data, total_chunks, filename, metadata): chunk_data 
            for chunk_data in batch_chunks
        }
        
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
