from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud
from .schemas import Order, OrderCreate, OrderUpdate, OrderUpdatePartial, OrderGet
from core.models import db_helper 

router = APIRouter(prefix="/orders", tags=['orders'])

@router.get('/{order_id}/', response_model=OrderGet)
async def order_get(order_id: int, session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.order_by_id(session=session, order_id=order_id)

@router.post('/', response_model=Order)
async def order_create(order_in: OrderCreate, session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.order_create(session=session, order_in=order_in)

@router.delete('/{order_id}/')
async def order_delete(order_id: int, session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.order_delete(session=session, order_id=order_id)

@router.patch('/{order_id}/')
async def order_update_partial(order_id: int, order_update: OrderUpdatePartial, session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.order_update_partial(session=session, order_id=order_id, order_update=order_update, partial=True)