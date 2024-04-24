from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel
from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import Mapped, Session, mapped_column

from APICore.result_models.cms.content_libraries import CMSContentLibrary
from APICore.result_models.cms.libraries import CMSLibrary, CMSLibraryBase
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal
from SQL_Connection.tables.tbl_cms_contentLibraries import create_new_content_library


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblCMSLibraries(Base):
    __tablename__ = "libraries"
    __table_args__ = {"schema": "cms"}

    id: Mapped[uuid4] = mapped_column(
        Uuid(), primary_key=True, index=True, nullable=False
    )
    addedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    addedById: Mapped[uuid4] = mapped_column(
        ForeignKey("accounts.users.id"), nullable=False
    )
    updatedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    updatedById: Mapped[uuid4] = mapped_column(
        ForeignKey("accounts.users.id"), nullable=False
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    type: Mapped[str] = mapped_column(String(15), nullable=False)
    description: Mapped[str] = mapped_column(String(2048), nullable=True)
    uploadContent: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    defaultRole: Mapped[str] = mapped_column(String(15), nullable=False)
    imageUri: Mapped[str] = mapped_column(String(2048), nullable=True)
    refreshedId: Mapped[uuid4] = mapped_column(
        ForeignKey("core.refreshed.id"), nullable=False
    )


## function to write to create a new entry item in the table
def create_new_library(
    item: CMSLibrary, refreshed, session: Session = None
) -> CMSLibrary:
    base_item = CMSLibraryBase(**item.model_dump(exclude_defaults=True))
    new_entry = TblCMSLibraries(
        **base_item.model_dump(exclude_defaults=True), refreshedId=refreshed.id
    )
    if session is None:
        db = SessionLocal()
    try:
        new_entry = read_db_library(item, db)
    except NotFoundError:
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
        if item.contentLibraries != []:
            [create_new_content_library(i, refreshed) for i in item.contentLibraries]
    finally:
        db.close()
    return new_entry


## function to read from the table
def read_db_library(item: CMSLibrary, session: Session) -> CMSLibrary:
    db_item = (
        session.query(TblCMSLibraries).filter(TblCMSLibraries.id == item.id).first()
    )
    if db_item is None:
        raise NotFoundError
    return db_item


## function to update the table
def update_library():
    pass


## function to delete from the table
def delete_library():
    pass
