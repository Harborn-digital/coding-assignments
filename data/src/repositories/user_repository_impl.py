from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from data.src.database.models.user import User
from domain.src.models.user import CreateUserDTO, UpdateUserDTO, UserDTO
from domain.src.repositories.user_repository import IUserRepository


class UserRepository(IUserRepository):
    """SQLAlchemy implementation of user repository."""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, user_data: CreateUserDTO) -> UserDTO:
        """Create a new user."""
        db_user = User(
            email=user_data.email,
            username=user_data.username,
            full_name=user_data.full_name,
            password=user_data.password,
        )
        self.session.add(db_user)
        await self.session.flush()
        await self.session.refresh(db_user)
        return UserDTO.model_validate(db_user)

    async def get_by_id(self, user_id: str) -> UserDTO | None:
        """Get user by ID."""
        result = await self.session.execute(select(User).where(User.id == int(user_id)))  # type: ignore[arg-type]
        user = result.scalar_one_or_none()
        return UserDTO.model_validate(user) if user else None

    async def get_all(self, skip: int = 0, limit: int = 100) -> list[UserDTO]:
        """Get all users with pagination."""
        result = await self.session.execute(select(User).offset(skip).limit(limit))
        users = result.scalars().all()
        return [UserDTO.model_validate(user) for user in users]

    async def update(self, user_id: int, user_data: UpdateUserDTO) -> UserDTO | None:
        """Update a user."""
        result = await self.session.execute(select(User).where(User.id == user_id))  # type: ignore[arg-type]
        user = result.scalar_one_or_none()

        if not user:
            return None

        update_data = user_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(user, field, value)

        await self.session.flush()
        await self.session.refresh(user)
        return UserDTO.model_validate(user)

    async def delete(self, user_id: int) -> bool:
        """Delete a user."""
        result = await self.session.execute(select(User).where(User.id == user_id))  # type: ignore[arg-type]
        user = result.scalar_one_or_none()

        if not user:
            return False

        await self.session.delete(user)
        await self.session.flush()
        return True

    async def get_by_email(self, email: str) -> UserDTO | None:
        """Get user by email."""
        result = await self.session.execute(select(User).where(User.email == email))  # type: ignore[arg-type]
        user = result.scalar_one_or_none()
        return UserDTO.model_validate(user) if user else None
