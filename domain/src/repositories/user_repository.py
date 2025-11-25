from abc import ABC, abstractmethod

from domain.src.models.user import CreateUserDTO, UpdateUserDTO, UserDTO


class IUserRepository(ABC):
    """User repository interface."""

    @abstractmethod
    async def create(self, user_data: CreateUserDTO) -> UserDTO:
        """Create a new user."""
        pass

    @abstractmethod
    async def get_by_id(self, user_id: str) -> UserDTO | None:
        """Get user by ID."""
        pass

    @abstractmethod
    async def get_all(self, skip: int = 0, limit: int = 100) -> list[UserDTO]:
        """Get all users with pagination."""
        pass

    @abstractmethod
    async def update(self, user_id: int, user_data: UpdateUserDTO) -> UserDTO | None:
        """Update a user."""
        pass

    @abstractmethod
    async def delete(self, user_id: int) -> bool:
        """Delete a user."""
        pass

    @abstractmethod
    async def get_by_email(self, email: str) -> UserDTO | None:
        """Get user by email."""
        pass
