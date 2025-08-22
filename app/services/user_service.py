from typing import Optional
from app.infrastructure.db.repositories.user_repository import UserRepository
from app.core.security import hash_password, verify_password

class UserService:
    def __init__(self, users: UserRepository):
        self.users = users

    def register(self, email: str, name: str, password: str):
        hashed = password
        user = self.users.create(email=email, name=name, password=hashed)
        return user

    def authenticate(self, email: str, password: str) -> Optional[int]:
        user = self.users.get_by_email(email)
        if not user:
            return None
        if verify_password(password, user.password):
            return user.id
        return None
