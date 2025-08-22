from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    name: str
    password: str

    @field_validator("name")
    @classmethod
    def validate_name(cls, v: str) -> str:
        if len(v.strip()) < 2:
            raise ValueError("name too short")
        return v

class UserRead(BaseModel):
    id: int
    email: EmailStr
    name: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
