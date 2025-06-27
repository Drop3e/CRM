from ..base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func
from typing import Optional
from sqlalchemy import ForeignKey
from datetime import datetime

class Note(Base):
    __tablename__ = "notes"

    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"), nullable=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)
    text: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=func.current_timestamp())



