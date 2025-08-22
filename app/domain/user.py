from dataclasses import dataclass
from datetime import datetime

@dataclass
class UserEntity:
    id: int | None
    email: str
    name: str
    password: str
    created_at: datetime | None = None
