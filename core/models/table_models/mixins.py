from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .user import User

class UserRelationMixin:
    
    _user_id_nullable: bool = False
    _user_id_unique: bool = False
    _user_back_populaties: str | None = None

    @declared_attr
    def user_id(cls) -> Mapped[int]:
        return mapped_column(ForeignKey('users.id'), nullable=cls._user_id_nullable, unique=cls._user_id_unique)
    
    @declared_attr
    def user(cls) -> Mapped["User"]:
        return relationship("User", back_populates=cls._user_back_populaties, foreign_keys=[user_id]) # type: ignore
    