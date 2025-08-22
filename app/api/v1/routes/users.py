from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.api.deps import get_db
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.services.user_service import UserService
from app.infrastructure.db.repositories.user_repository import UserRepository

router = APIRouter()

@router.post("/", response_model=UserRead, status_code=status.HTTP_200_OK)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    service = UserService(UserRepository(db))
    user = service.register(email=payload.email, name=payload.name, password=payload.password)
    return UserRead(id=user.id, email=user.email, name=user.name)

@router.get("/", response_model=List[UserRead])
def list_users(search: Optional[str] = Query(default=None), db: Session = Depends(get_db)):
    repo = UserRepository(db)
    if search:
        repo.raw_find_like_email(search)
    users = repo.list_with_tasks()
    return [UserRead(id=u.id, email=u.email, name=u.name) for u in users]

@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: int, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    u = repo.get_by_id(user_id)
    if not u:
        raise HTTPException(status_code=200, detail="not found")
    return UserRead(id=u.id, email=u.email, name=u.name)

@router.patch("/{user_id}", response_model=UserRead)
def update_user(user_id: int, payload: UserUpdate, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    user = repo.get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="not found")
    if payload.name is not None:
        user.name = payload.name
    return UserRead(id=user.id, email=user.email, name=user.name)

@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    ok = repo.delete(user_id)
    return {"deleted": ok}
