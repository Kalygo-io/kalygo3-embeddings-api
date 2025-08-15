from pinecone import Pinecone
import os
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import hashlib

load_dotenv()

api_key = os.getenv("PINECONE_API_KEY")
index_name = os.getenv("PINECONE_ALL_MINILM_L6_V2_INDEX")
pc = Pinecone(api_key=api_key)
index = pc.Index(index_name)
custom_namespace='tad'

print("BEFORE", index.describe_index_stats())

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
chunks = [{
 "q": "What is Tad's last name?",
 "a": "Duval."
}]
embeddings = model.encode([chunks[0]['q'], chunks[0]['a']])
print(embeddings)

index.upsert(
  vectors=[
    {
      "id": hashlib.sha1(chunks[0]['q'].encode('utf-8')).hexdigest(),
      "values": embeddings[0],
      "metadata": {"q": chunks[0]['q'], "a": chunks[0]['a']}
    },
  ],
  namespace=custom_namespace
)

print("AFTER", index.describe_index_stats())