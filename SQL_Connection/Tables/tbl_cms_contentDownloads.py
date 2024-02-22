from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel
from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from SQL_Connection.db_connection import Base


## creating the pydantic BaseModel
class CMSContentDownload(BaseModel):
    id: UUID
    contentId: UUID
    downloadedAt: datetime
    downloadedById: UUID
    refreshedId: UUID


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblCMSContentDownloads(Base):
    __tablename__ = "contentDownloads"
    __table_args__ = {"schema": "cms"}

    id: Mapped[uuid4] = mapped_column(
        Uuid(), primary_key=True, index=True, nullable=False
    )
    contentId: Mapped[uuid4] = mapped_column(
        ForeignKey("cms.contents.id"), nullable=False
    )
    downloadedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    downloadedById: Mapped[uuid4] = mapped_column(
        ForeignKey("accounts.users.id"), nullable=False
    )
    refreshedId: Mapped[uuid4] = mapped_column(
        ForeignKey("core.refreshed.id"), nullable=False
    )


## function to write to create a new entry item in the table
def create_new_entry():
    pass


## function to read from the table
def read_entry():
    pass


## function to update the table
def update_entry():
    pass


## function to delete from the table
def delete_entry():
    pass
