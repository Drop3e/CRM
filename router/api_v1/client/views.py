from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud
from .schemas import Client, ClientCreate, ClientUpdate, ClientUpdatePartial, ClientGet
from core.models import db_helper 


router = APIRouter(prefix="/clients", tags=["clients"])

@router.get("/", response_model=list[ClientGet])
async def get_client(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_clients(session=session)

@router.get("/{client_id}/", response_model=ClientGet)
async def client_by_id(client_id: int, session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    client = await crud.client_by_id(client_id=client_id, session=session)
    if client:
        return client
    raise HTTPException(status_code=404, detail="Client not found")


@router.post("/", response_model=Client)
async def create_client(
    client_in: ClientCreate, 
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
    ):
    
    return await crud.create_client(session=session, client_in=client_in)
    
@router.patch("/{client_id}/")
async def update_client(
    client_update: ClientUpdatePartial, 
    client_id: int, 
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
    ):
    return await crud.client_update(
        client_update=client_update,
        client_id=client_id,
        session=session,
        partial=True,
    )