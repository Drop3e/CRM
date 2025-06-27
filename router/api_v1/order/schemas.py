from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Literal, Optional
from datetime import datetime

class OrderBase(BaseModel):
    client_id: int
    created_by: int
    description: str
    amount: int
    status: Literal['pending', 'in progress', 'done', 'cancelled']


class OrderGet(OrderBase):
    created_at: datetime


class OrderCreate(OrderBase): pass


class OrderUpdate(OrderBase): pass


class OrderUpdatePartial(BaseModel):
    client_id: int | None = None
    created_by: int | None = None
    description: str | None = None
    amount: int | None = None
    status: Literal['pending', 'in progress', 'done', 'cancelled'] | None = None

class Order(OrderBase):
    model_config = ConfigDict(from_attributes=True)

    id: int