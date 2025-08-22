from typing import Generator
from app.infrastructure.db.session import SessionLocal, engine
from app.infrastructure.db.base import Base

def get_db() -> Generator:
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        pass
