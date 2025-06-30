from typing import TYPE_CHECKING
from ..base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func
from typing import Optional
from sqlalchemy import ForeignKey
from datetime import datetime

from .mixins import UserRelationMixin

if TYPE_CHECKING:
    from .user import User
    from .client import Client

class Note(Base):
    __tablename__ = "notes"

    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"), nullable=False)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), nullable=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    text: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=func.current_timestamp())


    user: Mapped["User"] = relationship("User", back_populates="notes", foreign_keys=[author_id])

    client: Mapped["Client"] = relationship("Client", back_populates="notes", foreign_keys=[client_id])

