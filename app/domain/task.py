from dataclasses import dataclass
from datetime import datetime

@dataclass
class TaskEntity:
    id: int | None
    title: str
    description: str | None
    status: str
    owner_id: int
    created_at: datetime | None = None
    due_date: datetime | None = None
