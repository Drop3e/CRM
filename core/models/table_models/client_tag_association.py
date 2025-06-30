from typing import TYPE_CHECKING
from sqlalchemy import Table, Column, Integer, ForeignKey, UniqueConstraint
from ..base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .client import Client
    from .tag import Tag

class ClientTagAssociation(Base):
    __tablename__ = "client_tag_associations"
    __table_args__ = (UniqueConstraint("tag_id", "client_id", name="idx_unique_tag_client"),)
    id: Mapped[int] = mapped_column(primary_key=True)
    
    tag_id: Mapped[int] = mapped_column(ForeignKey("tags.id"))
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"))

    tag: Mapped["Tag"] = relationship(back_populates='clients_details')
    client: Mapped["Client"] = relationship(back_populates='tags_details')