from datetime import datetime
from typing import Iterable, Optional
from app.infrastructure.db.repositories.task_repository import TaskRepository

class TaskService:
    def __init__(self, tasks: TaskRepository):
        self.tasks = tasks

    def create_for_user(self, owner_id: int, title: str, description: str | None, due_date: datetime | None):
        return self.tasks.create(title=title, description=description, owner_id=owner_id, due_date=due_date)

    def list_for_owner(self, owner_id: int) -> Iterable:
        return self.tasks.list_for_owner(owner_id)

    def update_status(self, task_id: int, status: str) -> Optional[int]:
        task = self.tasks.update_status(task_id, status)
        return task.id if task else None
