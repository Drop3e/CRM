from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud
from .schemas import User, UserCreate, UserUpdate, UserUpdatePartial
from core.models import db_helper 

router = APIRouter(prefix='/users',tags=['users'])

@router.post("/", response_model=User)
async def create_user(
    user_in: UserCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_user(user_in=user_in, session=session)
    

@router.get("/", response_model=list[User])
async def get_users(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_users(session=session)

@router.get("/{user_id}")
async def user_by_id(user_id: int, session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    user = await crud.user_by_id(user_id=user_id, session=session)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return user 
