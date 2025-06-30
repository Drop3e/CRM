import asyncio
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, User, Order, Note, Client, Tag, ClientTagAssociation


async def create_teg(session: AsyncSession, name: str):
    tag = Tag(name=name)
    session.add(tag)
    await session.commit()
    print('Tag: ', tag)
    return tag

async def get_tag_by_name(session: AsyncSession, name: str) -> Tag | None:
    stmt = select(Tag).where(Tag.name == name)
    # result: Result | None = await session.execute(stmt)
    # tag: Tag | None = result.scalar_one_or_none()
    tag: Tag | None = await session.scalar(stmt)
    # print('tag found =', tag)
    return tag

async def get_client_by_name(session: AsyncSession, name: str) -> Client | None:
    stmt = select(Client).where(Client.name == name)
    client: Client | None = await session.scalar(stmt)

    return client

async def create_user(
        session: AsyncSession, 
        username: str, 
        role: str,
        email: str,
        hashed_password: str,
        # is_active: str
        ) -> User:
    user = User(username=username, role=role, email=email, hashed_password=hashed_password)
    session.add(user)
    await session.commit()
    print(user)
    return user

async def create_client(session: AsyncSession, name: str, description: str, created_by: int ):
    client = Client(name=name, description=description, created_by=created_by)
    session.add(client)
    await session.commit()
    return client

async def create_tag_and_client_assoc(session: AsyncSession):
    tag = await get_tag_by_name(session, "English")
    client = await get_client_by_name(session, "Daniel")
    assoc = ClientTagAssociation(client=client, tag=tag)
    session.add(assoc)
    await session.commit()
    return assoc

async def get_client_with_tag(session: AsyncSession):
    stmt = select(Client).options(selectinload(Client.tags_details).selectinload(ClientTagAssociation.tag)).order_by(Client.id)
    client = await session.scalar(stmt)
    for assoc in client.tags_details:
        print(assoc.tag.name)


async def mein_relations(session: AsyncSession):
    # await create_teg(session, "English")
    # await get_tag_by_name(session=session, name='UpWork')
    # await create_user(session, "John", "admin", 'gmail.com', 'sdadasdasd')
    # await create_client(session, 'Daniel', '22 years old', 1)
    # await create_tag_and_client_assoc(session)
    await get_client_with_tag(session)
    pass

async def main():

    async with db_helper.session_factory() as session:
        await mein_relations(session=session)
        # await demo_m2m(session=session)
            
if __name__ == "__main__":
    asyncio.run(main())

