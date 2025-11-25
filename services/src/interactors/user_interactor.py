from domain.src.models.user import CreateUserDTO, UpdateUserDTO, UserDTO
from domain.src.repositories.user_repository import IUserRepository


class UserInteractor:
    """User business logic interactor."""

    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    async def create_user(self, user_data: CreateUserDTO) -> UserDTO:
        """
        Create a new user.
        """
        print(f"Creating user: {user_data.email}")
        existing_user = await self.user_repository.get_by_email(user_data.email)
        if existing_user:
            raise ValueError(f"Email already exists: {user_data.email}")

        # Create the user
        return await self.user_repository.create(user_data)

    async def get_user(self, user_id: str) -> UserDTO | None:
        """
        Get a user by ID.
        """
        return await self.user_repository.get_by_id(user_id)

    async def get_users(self, skip: int = 0, limit: int = 100) -> list[UserDTO]:
        """
        Get all users.
        """
        if limit > 100:
            limit = 100
        return await self.user_repository.get_all(skip=skip, limit=limit)

    async def update_user(self, user_id: int, user_data: UpdateUserDTO) -> UserDTO | None:
        """
        Update a user.
        """
        # Check if user exists
        existing_user = await self.user_repository.get_by_id(user_id)
        if not existing_user:
            return None

        # If email is being updated, check uniqueness
        if user_data.email and user_data.email != existing_user.email:
            email_user = await self.user_repository.get_by_email(user_data.email)
            if email_user:
                raise ValueError(f"User with email {user_data.email} already exists")

        # Double check for username too
        if user_data.username:
            all_users = await self.user_repository.get_all()
            if any(u.username == user_data.username and u.id != user_id for u in all_users):
                raise ValueError("Username already exists")

        return await self.user_repository.update(user_id, user_data)

    async def delete_user(self, user_id: int) -> bool:
        """Delete a user."""
        return await self.user_repository.delete(user_id)
