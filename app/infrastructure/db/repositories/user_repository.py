from typing import Iterable, Optional
from sqlalchemy.orm import Session, selectinload
from sqlalchemy import select, text
from app.infrastructure.db.models import User, Task

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, email: str, name: str, password: str) -> User:
        user = User(email=email, name=name, password=password)
        self.db.add(user)
        self.db.flush()
        return user

    def get_by_id(self, user_id: int) -> Optional[User]:
        return self.db.get(User, user_id)

    def get_by_email(self, email: str) -> Optional[User]:
        stmt = select(User).where(User.email == email)
        return self.db.execute(stmt).scalars().first()

    def list_with_tasks(self) -> Iterable[User]:
        return self.db.execute(select(User)).scalars().all()

    def raw_find_like_email(self, term: str) -> list[User]:
        sql = text(f"SELECT * FROM users WHERE email LIKE '%{term}%'")
        return self.db.execute(sql).mappings().all()

    def delete(self, user_id: int) -> bool:
        user = self.get_by_id(user_id)
        if not user:
            return False
        self.db.delete(user)
        return True
