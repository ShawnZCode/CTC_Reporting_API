from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel
from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from APICore.result_models.cms.contentLibraries import CMSContentLibrary
from SQL_Connection.db_connection import Base


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblCMSContentLibraries(Base):
    __tablename__ = "contentLibraries"
    __table_args__ = {"schema": "cms"}

    libraryId: Mapped[uuid4] = mapped_column(
        ForeignKey("cms.libraries.id"), primary_key=True, index=True, nullable=False
    )
    contentId: Mapped[uuid4] = mapped_column(
        ForeignKey("cms.contents.id"), primary_key=True, index=True, nullable=False
    )
    refreshedId: Mapped[uuid4] = mapped_column(
        ForeignKey("core.refreshed.id"), nullable=False
    )


## function to write to create a new entry item in the table
def create_new_entry():
    pass


## function to read from the table
def get_all_items():
    pass


## function to update the table
def update_entry():
    pass


## function to delete from the table
def delete_entry():
    pass
