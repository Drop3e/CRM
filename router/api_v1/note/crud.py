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
from core.models import Note

from .schemas import NoteGet, NoteUpdate, NoteCreate, NoteUpdatePartial


async def note_by_id(session: AsyncSession, note_id: int) -> NoteGet:
    return await session.get(Note, note_id)


async def note_create(session: AsyncSession, note_in: NoteCreate):
    note = Note(**note_in.model_dump())
    session.add(note)
    await session.commit()
    return note

async def note_update(session: AsyncSession, note_id: int, update_in: NoteUpdate) -> NoteUpdate:
    note = await note_by_id(session=session, note_id=note_id)
    for name, value in update_in.model_dump().items():
        setattr(note, name, value)
    await session.commit()
    return note