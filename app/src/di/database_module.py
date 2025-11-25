from collections.abc import AsyncGenerator
from functools import lru_cache

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.src.config import settings


@lru_cache
def get_engine():
    """Get database engine (singleton)."""
    return create_async_engine(
        settings.DATABASE_URL,
        echo=settings.DEBUG,
        future=True,
        pool_size=50,
        max_overflow=100,
    )


@lru_cache
def get_session_factory():
    """Get session factory (singleton)."""
    engine = get_engine()
    return async_sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )


async def get_db_session() -> AsyncGenerator[AsyncSession]:
    """Get database session dependency."""
    session_factory = get_session_factory()
    async with session_factory() as session:
        yield session
        await session.commit()
