from datetime import datetime

from pydantic import BaseModel, ConfigDict


class UserDTO(BaseModel):
    """User domain model."""

    id: int | None = None
    email: str
    username: str
    full_name: str | None = None
    is_active: bool = True
    password: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)


class CreateUserDTO(BaseModel):
    """DTO for creating a new user."""

    email: str
    username: str
    full_name: str | None = None
    password: str


class UpdateUserDTO(BaseModel):
    """DTO for updating a user."""

    email: str | None = None
    username: str | None = None
    full_name: str | None = None
    is_active: bool | None = None
