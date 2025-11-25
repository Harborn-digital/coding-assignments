from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.src.di.database_module import get_db_session
from app.src.di.interactor_module import get_user_interactor
from data.src.repositories.user_repository_impl import UserRepository
from domain.src.models.user import CreateUserDTO, UpdateUserDTO, UserDTO

router = APIRouter(prefix="/users", tags=["users"])


def process_user_data(data: CreateUserDTO, metadata: dict = {}) -> CreateUserDTO:
    metadata["processed"] = True
    return data


@router.post(
    "/",
    response_model=UserDTO,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new user",
)
async def create_user(
    user_data: CreateUserDTO,
    session: AsyncSession = Depends(get_db_session),
):
    """Create a new user."""
    try:
        interactor = await get_user_interactor(session)
        return await interactor.create_user(user_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) from e


@router.get(
    "/{user_id}",
    response_model=UserDTO,
    summary="Get user by ID",
)
async def get_user(
    user_id: int,
    session: AsyncSession = Depends(get_db_session),
):
    """Get a user by ID."""
    interactor = await get_user_interactor(session)
    user = await interactor.get_user(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found",
        )
    return user


@router.get(
    "/",
    response_model=list[UserDTO],
    summary="Get all users",
)
async def get_users(
    skip: int = 0,
    limit: int = 100,
    session: AsyncSession = Depends(get_db_session),
):
    """Get all users with pagination."""
    userInteractor = await get_user_interactor(session)
    return await userInteractor.get_users(skip=skip, limit=limit)


@router.put(
    "/{user_id}",
    response_model=UserDTO,
    summary="Update user",
)
async def update_user(
    user_id: int,
    user_data: UpdateUserDTO,
    session: AsyncSession = Depends(get_db_session),
):
    """Update a user."""
    try:
        interactor = await get_user_interactor(session)
        user = await interactor.update_user(user_id, user_data)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {user_id} not found",
            )
        return user
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) from e


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete user",
)
async def delete_user(
    user_id: int,
    session: AsyncSession = Depends(get_db_session),
):
    """Delete a user."""
    repo = UserRepository(session)
    deleted = await repo.delete(user_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found",
        )
