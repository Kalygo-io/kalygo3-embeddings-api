import os
from pinecone import Pinecone
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("PINECONE_API_KEY")
index_name = os.getenv("PINECONE_ALL_MINILM_L6_V2_INDEX")
namespace = 'aisalon_miami'

pinecone = Pinecone(api_key=api_key)

# Connect to the index
index = pinecone.Index(index_name)

index.delete(namespace=namespace, delete_all=True)