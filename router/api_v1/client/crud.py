"""
Create
Read
Update
Delete
"""

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Client

from .schemas import ClientCreate, ClientUpdate, ClientUpdatePartial, ClientGet

async def create_client(session: AsyncSession, client_in: ClientCreate) -> Client:
    client = Client(**client_in.model_dump())
    session.add(client)
    await session.commit()
    return client

async def get_clients(session: AsyncSession) -> list[ClientGet]:
    stmt = select(Client).order_by(Client.id)
    resurl: Result = await session.execute(stmt)
    clients = resurl.scalars().all()
    return clients

async def client_by_id(session: AsyncSession, client_id: int) -> ClientGet | None:
    return await session.get(Client, client_id) 

async def client_update(
    session: AsyncSession,
    client_update: ClientUpdatePartial,
    client_id: int,
    partial: bool = None,  
) -> Client:
    client = await client_by_id(session=session, client_id=client_id)
    for name, value in client_update.model_dump(exclude_unset=partial).items():
        setattr(client, name, value)
    await session.commit()
    return client


async def client_delete(session: AsyncSession, client_id: int):
    client = client_by_id(session=session, client_id=client_id)
    await session.delete(client)
    await session.commit()
    