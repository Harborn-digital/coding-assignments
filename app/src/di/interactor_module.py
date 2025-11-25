from sqlalchemy.ext.asyncio import AsyncSession

from data.src.repositories.user_repository_impl import UserRepository
from services.src.interactors.user_interactor import UserInteractor


async def get_user_interactor(session: AsyncSession) -> UserInteractor:
    """Get user interactor dependency."""
    repository = UserRepository(session)
    return UserInteractor(repository)
