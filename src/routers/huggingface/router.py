from fastapi import APIRouter, Response, HTTPException
from sentence_transformers import SentenceTransformer
import logging
import os
import threading
import time

from src.core.schemas.EmbeddingInput import EmbeddingInput
from src.deps import jwt_dependency, auth_dependency

# Configure logging to reduce verbose output
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Reduce verbose output from sentence_transformers
logging.getLogger("sentence_transformers").setLevel(logging.WARNING)
logging.getLogger("transformers").setLevel(logging.WARNING)
logging.getLogger("torch").setLevel(logging.WARNING)

router = APIRouter(
    prefix='/huggingface',
    tags=['huggingface']
)

# Global model instance with proper locking
_embedding_model = None
_model_loading_lock = threading.Lock()
_last_loading_attempt = 0
_loading_cooldown = 30  # seconds

def get_embedding_model():
    """Get or create the embedding model instance with retry logic"""
    global _embedding_model, _last_loading_attempt
    
    # If model is already loaded, return it
    if _embedding_model is not None:
        return _embedding_model
    
    # Check if we're in cooldown period
    current_time = time.time()
    if current_time - _last_loading_attempt < _loading_cooldown:
        raise HTTPException(
            status_code=503,
            detail="Model is currently loading. Please try again in a few seconds."
        )
    
    # Use lock to prevent multiple simultaneous loading attempts
    with _model_loading_lock:
        # Double-check if model was loaded while waiting for lock
        if _embedding_model is not None:
            return _embedding_model
        
        _last_loading_attempt = current_time
        
        try:
            logger.info("Loading all-MiniLM-L6-v2 model...")
            # Load model with explicit CPU device and proper error handling
            _embedding_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
            
            # Force model to CPU to avoid any device issues
            if hasattr(_embedding_model, 'to'):
                _embedding_model.to('cpu')
            
            logger.info("✅ Model loaded successfully and cached in memory")
            return _embedding_model
            
        except Exception as e:
            logger.error(f"Failed to load model: {e}")
            # Reset the model to None so we can retry
            _embedding_model = None
            raise HTTPException(
                status_code=500, 
                detail=f"Failed to load embedding model. Please try again. Error: {str(e)}"
            )

@router.post("/embedding")
def create_embeddings(response: Response, textToEmbed: EmbeddingInput, user: auth_dependency):
    print("=" * 80)
    print("🔵 create_embeddings: Function called")
    print(f"🔵 create_embeddings: user = {user}")
    print(f"🔵 create_embeddings: auth_type = {user.get('auth_type', 'unknown')}")
    print(f"🔵 create_embeddings: textToEmbed = {textToEmbed}")
    print(f"🔵 create_embeddings: textToEmbed.input = {textToEmbed.input if hasattr(textToEmbed, 'input') else 'N/A'}")
    
    try:
        print("🔵 create_embeddings: About to get embedding model...")
        embedding_model = get_embedding_model()
        print(f"🔵 create_embeddings: Got embedding model: {embedding_model}")
        
        # Generate embeddings - ensure input is a list
        print(f"🔵 create_embeddings: About to encode input: {[textToEmbed.input]}")
        embeddings = embedding_model.encode([textToEmbed.input], show_progress_bar=False)
        print(f"🔵 create_embeddings: Generated embeddings, shape: {embeddings.shape if hasattr(embeddings, 'shape') else 'N/A'}")
        
        embeddings_list = embeddings.tolist()
        print(f"🔵 create_embeddings: Converted to list, length: {len(embeddings_list)}")
        print("🔵 create_embeddings: About to return response")
        return {"embedding": embeddings_list, "model": "sentence-transformers/all-MiniLM-L6-v2"}
    except HTTPException as http_ex:
        # Re-raise HTTP exceptions as-is
        print(f"🔴 create_embeddings: HTTPException caught - status_code: {http_ex.status_code}, detail: {http_ex.detail}")
        raise
    except Exception as e:
        print(f"🔴 create_embeddings: Exception caught - type: {type(e).__name__}, message: {str(e)}")
        logger.error(f"Error generating embeddings: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to generate embeddings: {str(e)}")

@router.get("/health")
def health_check():
    """Health check endpoint to verify model status"""
    try:
        model = get_embedding_model()
        return {
            "status": "healthy",
            "model": "sentence-transformers/all-MiniLM-L6-v2",
            "model_loaded": model is not None
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "error": str(e),
            "model_loaded": False
        }