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

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})" # это для отладки
    
    def __repr__(self):
        return str(self)