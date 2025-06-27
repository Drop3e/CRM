from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Literal, Optional


class UserBase(BaseModel):

    email: EmailStr
    username: str
    hashed_password: str
    role: Literal["admin", "manager", "user"]
    is_active: bool


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserUpdatePartial(BaseModel):
    
    email: EmailStr | None = None
    username: str | None = None
    hashed_password: str | None = None
    role: Literal["admin", "manager", "user"] | None = None
    is_active: bool | None = None


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int