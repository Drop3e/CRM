from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import CheckConstraint, func
from typing import Optional
from ..base import Base
from datetime import datetime

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

    __table_args__ = (
        CheckConstraint("role IN ('admin', 'manager', 'user')", name="check_role"),
    )