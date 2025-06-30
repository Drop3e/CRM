from typing import TYPE_CHECKING
from ..base import Base
from typing import Optional
from sqlalchemy import ForeignKey, CheckConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

if TYPE_CHECKING:
    from .user import User
    from .client import Client

class Order(Base):
    __tablename__ = "orders"

    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"), nullable=False)
    created_by: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    amount: Mapped[int] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=func.current_timestamp())
    # updated_at: Mapped[datetime] = mapped_column(default_factory=datetime.utcnow, onupdate=datetime.utcno)

    user: Mapped["User"] = relationship('User', back_populates='orders', foreign_keys=[created_by])

    client: Mapped["Client"] = relationship('Client', back_populates='orders', foreign_keys=[client_id])

    __table_args__ = (
    CheckConstraint("status IN('pending', 'in progress', 'done', 'cancelled')", name="check_status"),
    )
