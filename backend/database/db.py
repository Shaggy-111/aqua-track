from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# For SQLite (local dev) - for production switch to PostgreSQL or MySQL
DATABASE_URL = "sqlite:///./aqua_track.db"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a session local factory
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base class for models
Base = declarative_base()

# Dependency for getting a DB session
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
