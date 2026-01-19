import secrets
import hashlib


def generate_api_key() -> str:
    """
    Generate a new API key with the format: kalygo_live_<random_string>
    Returns the plaintext API key (store the hash, not this!)
    """
    # Generate 32 bytes of random data, convert to hex (64 chars)
    random_part = secrets.token_hex(32)
    api_key = f"kalygo_live_{random_part}"
    return api_key


def hash_api_key(api_key: str) -> str:
    """
    Hash an API key using SHA-256.
    This is what gets stored in the database.
    """
    return hashlib.sha256(api_key.encode()).hexdigest()


def verify_api_key(plaintext_key: str, hashed_key: str) -> bool:
    """
    Verify a plaintext API key against a stored hash.
    Returns True if they match, False otherwise.
    """
    return hash_api_key(plaintext_key) == hashed_key


def get_key_prefix(api_key: str, length: int = 20) -> str:
    """
    Extract the prefix of an API key for fast database lookups.
    Default length is 20 characters.
    """
    return api_key[:length] if len(api_key) >= length else api_key
