from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# ✅ Use correct relative path for SQLite database file
SQLALCHEMY_DATABASE_URL = "sqlite:///./aqua_track.db"  # One level above 'database' folder

# ✅ Create SQLAlchemy engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# ✅ Create session factory
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# ✅ Base class for SQLAlchemy models
Base = declarative_base()

# ✅ Dependency function to get a DB session
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
