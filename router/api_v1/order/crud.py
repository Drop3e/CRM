"""
Create
Read
Update
Delete
"""
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Order

from .schemas import OrderCreate, OrderUpdate, OrderGet, OrderUpdatePartial

async def order_by_id(session: AsyncSession, order_id: int) -> OrderGet | None:
    return await session.get(Order, order_id)
    

async def order_create(session: AsyncSession, order_in: OrderCreate) -> Order:
    order = Order(**order_in.model_dump())
    session.add(order)
    await session.commit()
    return order

async def order_delete(session: AsyncSession, order_id: int):
    order_for_delete = await order_by_id(session=session, order_id=order_id)
    await session.delete(order_for_delete)
    await session.commit()
    return order_for_delete

async def order_update_partial(
    session: AsyncSession,
    order_update: OrderUpdatePartial,
    order_id: int,
    partial: bool = None,
):
    order = await order_by_id(session=session, order_id=order_id)
    for name, value in order_update.model_dump(exclude_unset=partial).items():
        setattr(order, name, value)
    await session.commit()
    return order