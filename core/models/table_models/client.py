from typing import TYPE_CHECKING
from ..base import Base
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import Optional

from .mixins import UserRelationMixin

if TYPE_CHECKING:
    from .user import User
    from .client_tag_association import ClientTagAssociation
    from .order import Order
    from .note import Note

class Client(UserRelationMixin, Base):
    __tablename__ = "clients"

    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[Optional[str]] = mapped_column(nullable=True)
    phone: Mapped[str] = mapped_column(nullable=True)
    description: Mapped[str] = mapped_column(nullable=False)
    created_by: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=func.current_timestamp())

    _user_back_populaties = "clients"
    tags_details: Mapped[list["ClientTagAssociation"]] = relationship(back_populates="client")

    orders: Mapped[list["Order"]] = relationship('Order', back_populates='client')
    notes: Mapped[list["Note"]] = relationship('Note', back_populates='client')
    

