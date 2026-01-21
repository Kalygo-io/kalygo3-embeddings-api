from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum as SQLEnum
from sqlalchemy.sql import func
from .database import Base
import enum


class ApiKeyStatus(enum.Enum):
    """Status of an API key"""
    ACTIVE = "active"
    REVOKED = "revoked"


class Account(Base):
    """Account model - represents a user account"""
    __tablename__ = "accounts"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)


class ApiKey(Base):
    """API Key model - stores hashed API keys for authentication"""
    __tablename__ = "api_keys"
    
    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False, index=True)
    key_prefix = Column(String, nullable=False, index=True)  # First 20 chars for lookup
    key_hash = Column(String, nullable=False)  # Hashed full key
    name = Column(String, nullable=True)  # Optional name/description
    status = Column(SQLEnum(ApiKeyStatus, values_callable=lambda x: [e.value for e in x], name='api_key_status_enum', create_type=False), nullable=False, default=ApiKeyStatus.ACTIVE, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    last_used_at = Column(DateTime(timezone=True), nullable=True)
