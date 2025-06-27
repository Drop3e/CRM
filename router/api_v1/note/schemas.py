from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Literal, Optional
from datetime import datetime


class Note(BaseModel):
    client_id: int
    order_id: int
    author_id: int
    text: str
    

class NoteGet(Note):
    created_at: datetime

class NoteCreate(Note): pass

class NoteUpdate(BaseModel): 
    text: str

class NoteUpdatePartial(BaseModel):
    client_id: int | None
    order_id: int | None
    author_id: int | None
    text: str | None
