from fastapi import APIRouter, Response, HTTPException
from sentence_transformers import SentenceTransformer
import logging
import os

from src.core.schemas.EmbeddingInput import EmbeddingInput
from src.deps import jwt_dependency

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

# Global model instance - load once at startup
_embedding_model = None
_model_loading_failed = False

def get_embedding_model():
    """Get or create the embedding model instance"""
    global _embedding_model, _model_loading_failed
    
    # If model loading previously failed, don't retry immediately
    if _model_loading_failed:
        raise HTTPException(
            status_code=500,
            detail="Embedding model failed to load. Please restart the service."
        )
    
    if _embedding_model is None:
        try:
            logger.info("Loading all-MiniLM-L6-v2 model...")
            # Load model without device specification to avoid meta tensor issues
            _embedding_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
            logger.info("✅ Model loaded successfully and cached in memory")
        except Exception as e:
            logger.error(f"Failed to load model: {e}")
            _model_loading_failed = True
            raise HTTPException(
                status_code=500, 
                detail=f"Failed to load embedding model. Error: {str(e)}"
            )
    
    return _embedding_model

@router.post("/embedding")
def create_embeddings(response: Response, textToEmbed: EmbeddingInput):  # Temporarily removed jwt: jwt_dependency
    try:
        embedding_model = get_embedding_model()
        
        # Generate embeddings - ensure input is a list
        embeddings = embedding_model.encode([textToEmbed.input], show_progress_bar=False)
        
        embeddings_list = embeddings.tolist()
        return {"embedding": embeddings_list, "model": "sentence-transformers/all-MiniLM-L6-v2"}
    except Exception as e:
        logger.error(f"Error generating embeddings: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to generate embeddings: {str(e)}")