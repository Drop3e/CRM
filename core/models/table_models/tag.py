from typing import TYPE_CHECKING
from ..base import Base
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship 
from datetime import datetime
from typing import Optional

if TYPE_CHECKING:
    from .client_tag_association import ClientTagAssociation

class Tag(Base):
    __tablename__ = "tags"
    
    name: Mapped[str] = mapped_column(unique=True, nullable=False)

    clients_details: Mapped[list["ClientTagAssociation"]] = relationship(back_populates='tag')
