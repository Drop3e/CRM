from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import CheckConstraint, func
from typing import Optional
from ..base import Base
from datetime import datetime

if TYPE_CHECKING:
    from .order import Order
    from .client import Client
    from .note import Note

# class Role: # how role we have
#     admin: str = "admin"
#     manager: str = "manager"
#     user: str = "user"

class User(Base):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(unique=True)
    username: Mapped[str] = mapped_column(nullable=False)
    hashed_password: Mapped[str]
    role: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(default=func.current_timestamp())

    notes: Mapped[list["Note"]] = relationship("Note", back_populates="user")
    clients: Mapped[list["Client"]] = relationship("Client", back_populates="user")
    orders: Mapped[list["Order"]] = relationship("Order", back_populates="user")

    __table_args__ = (
        CheckConstraint("role IN ('admin', 'manager', 'user')", name="check_role"),
    )

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r})" # это для отладки
    
    def __repr__(self):
        return str(self)