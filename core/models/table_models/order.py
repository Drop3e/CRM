from ..base import Base
from typing import Optional
from sqlalchemy import ForeignKey, CheckConstraint, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class Order(Base):
    __tablename__ = "orders"

    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"), nullable=False)
    created_by: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    amount: Mapped[int] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=func.current_timestamp())
    # updated_at: Mapped[datetime] = mapped_column(default_factory=datetime.utcnow, onupdate=datetime.utcno)

    __table_args__ = (
    CheckConstraint("status IN('pending', 'in progress', 'done', 'cancelled')", name="check_status"),
    )
