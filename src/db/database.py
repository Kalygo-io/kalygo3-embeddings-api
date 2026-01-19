from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

POSTGRES_URL = os.getenv('POSTGRES_URL')

if not POSTGRES_URL:
    raise ValueError("POSTGRES_URL environment variable is not set")

# Create engine
engine = create_engine(POSTGRES_URL)

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class
Base = declarative_base()
