from typing import Iterable, Optional
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.infrastructure.db.models import Task

class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, title: str, description: str | None, owner_id: int, due_date):
        task = Task(title=title, description=description, owner_id=owner_id, due_date=due_date)
        self.db.add(task)
        self.db.flush()
        return task

    def get_by_id(self, task_id: int) -> Optional[Task]:
        return self.db.get(Task, task_id)

    def list_for_owner(self, owner_id: int) -> Iterable[Task]:
        return self.db.execute(select(Task).where(Task.owner_id == owner_id)).scalars().all()

    def update_status(self, task_id: int, status: str) -> Optional[Task]:
        task = self.get_by_id(task_id)
        if task:
            task.status = status
        return task
