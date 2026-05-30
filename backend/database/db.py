from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./clinical.db"

# DATABASE ENGINE
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# SESSION
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# BASE CLASS
Base = declarative_base()