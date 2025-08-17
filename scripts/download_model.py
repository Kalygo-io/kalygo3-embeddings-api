#!/usr/bin/env python3
"""
Download all-MiniLM-L6-v2 model locally
"""
from sentence_transformers import SentenceTransformer
import os

def download_model():
    """Download the model and test it"""
    print("📥 Downloading all-MiniLM-L6-v2 model...")
    
    try:
        # Download the model
        model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2', device='cpu')
        print("✅ Model downloaded successfully!")
        
        # Test the model
        test_text = "This is a test sentence for embedding generation."
        embedding = model.encode([test_text])
        
        print(f"✅ Model tested successfully!")
        print(f"📊 Embedding dimension: {len(embedding[0])}")
        print(f"📊 Test embedding shape: {embedding.shape}")
        
        # Show where the model is cached
        cache_dir = os.path.expanduser("~/.cache/huggingface/hub")
        print(f"📁 Model cached at: {cache_dir}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error downloading model: {e}")
        return False

if __name__ == "__main__":
    download_model() 