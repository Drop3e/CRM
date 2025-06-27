from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Literal, Optional
from datetime import datetime

class ClientBase(BaseModel):
    
    name: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    created_by: int
    description: str


class ClientGet(ClientBase):
    created_at: datetime


class ClientCreate(ClientBase): pass


class ClientUpdate(ClientBase): pass


class ClientUpdatePartial(BaseModel):

    name: str | None = None
    email: Optional[EmailStr] | None = None
    phone: Optional[str] | None = None
    created_by: int | None = None
    description: str | None = None


class Client(ClientBase):
    model_config = ConfigDict(from_attributes=True)

    id: int