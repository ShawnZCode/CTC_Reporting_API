from sqlalchemy import DateTime, Uuid, String, Boolean, Float, Integer, ForeignKey
from uuid import UUID, uuid4
from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped
from SQL_Connection.db_connection import Base
from pydantic import BaseModel
from typing import Optional

## creating the pydantic BaseModel
class CMS_ContentLibraries(BaseModel):
    libraryId: UUID
    contentId: UUID
    refreshedId: UUID

## Using SQLAlchemy2.0 generate Table with association to the correct schema
class Tbl_CMS_ContentLibraries(Base):
    __tablename__ = 'contentLibraries'
    __table_args__ = {"schema": "cms"}

    libraryId: Mapped[uuid4] = mapped_column(ForeignKey('cms.libraries.id'), primary_key=True, index=True, nullable=False)
    contentId: Mapped[uuid4] = mapped_column(ForeignKey('cms.contents.id'), primary_key=True, index=True, nullable=False)
    refreshedId: Mapped[uuid4] = mapped_column(ForeignKey('core.refreshed.id'), nullable=False)

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