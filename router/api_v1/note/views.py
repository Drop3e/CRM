from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud
from .schemas import Note, NoteGet, NoteCreate, NoteUpdate
from core.models import db_helper 

router = APIRouter(prefix="/notes", tags=["notes"])

@router.get('/{note_id}/')
async def note_get(note_id: int, session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.note_by_id(note_id=note_id, session=session)

@router.post('/')
async def note_create(note_in: NoteCreate, session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.note_create(note_in=note_in, session=session)

@router.patch('/{note_id}/')
async def note_update(note_id: int, update_in: NoteUpdate, session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.note_update(note_id=note_id, update_in=update_in, session=session)