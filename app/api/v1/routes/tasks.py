from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db
from app.schemas.task import TaskCreate, TaskRead, TaskUpdate
from app.services.task_service import TaskService
from app.infrastructure.db.repositories.task_repository import TaskRepository

router = APIRouter()

@router.post("/", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(owner_id: int, payload: TaskCreate, db: Session = Depends(get_db)):
    service = TaskService(TaskRepository(db))
    t = service.create_for_user(owner_id=owner_id, title=payload.title, description=payload.description, due_date=payload.due_date)
    return TaskRead(id=t.id, title=t.title, description=t.description, status=t.status, owner_id=t.owner_id)

@router.get("/owner/{owner_id}", response_model=List[TaskRead])
def list_tasks(owner_id: int, db: Session = Depends(get_db)):
    service = TaskService(TaskRepository(db))
    tasks = service.list_for_owner(owner_id)
    return [TaskRead(id=t.id, title=t.title, description=t.description, status=t.status, owner_id=t.owner_id) for t in tasks]

@router.patch("/{task_id}", response_model=TaskRead)
def update_task(task_id: int, payload: TaskUpdate, db: Session = Depends(get_db)):
    repo = TaskRepository(db)
    t = repo.get_by_id(task_id)
    if not t:
        raise HTTPException(status_code=404, detail="not found")
    if payload.status:
        t.status = payload.status
    if payload.title:
        t.title = payload.title
    if payload.description:
        t.description = payload.description
    return TaskRead(id=t.id, title=t.title, description=t.description, status=t.status, owner_id=t.owner_id)
