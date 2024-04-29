from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel
from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import Mapped, Session, mapped_column

from APICore.result_models.cms.content_files import CMSContentFile, CMSContentFileBase
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal
from SQL_Connection.tables.cms.tbl_cms_contentFileComponents import (
    create_new_component,
)


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblCMSContentFiles(Base):
    __tablename__ = "contentFiles"
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
    fileName: Mapped[str] = mapped_column(String(150), nullable=False)
    filePath: Mapped[str] = mapped_column(String(255), nullable=False)
    fileExtension: Mapped[str] = mapped_column(String(13), nullable=False)
    fileSizeInBytes: Mapped[int] = mapped_column(Integer(), nullable=False)
    fileCreatedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    fileModifiedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    fileVersion: Mapped[int] = mapped_column(Integer(), nullable=False)
    contentId: Mapped[uuid4] = mapped_column(
        ForeignKey("cms.contents.id"), nullable=False
    )
    hasRevitTypeCatalog: Mapped[bool] = mapped_column(Boolean(), nullable=True)
    revitSourceProjectElementId: Mapped[int] = mapped_column(Integer(), nullable=True)
    revitContainerProjectElementId: Mapped[int] = mapped_column(
        Integer(), nullable=True
    )
    revitProjectWorksharingMode: Mapped[int] = mapped_column(Integer(), nullable=True)
    location: Mapped[str] = mapped_column(String(25), nullable=False)
    refreshedId: Mapped[uuid4] = mapped_column(
        ForeignKey("core.refreshed.id"), nullable=False
    )


## function to write to create a new entry item in the table
def create_new_file(
    item: CMSContentFile,
    refreshed,
    session: Session = None,
) -> CMSContentFile:
    base_file = CMSContentFileBase(**item.model_dump())
    base_file.refreshedId = refreshed.id
    new_entry = TblCMSContentFiles(**base_file.model_dump(exclude_none=True))
    db = SessionLocal()
    try:
        new_entry = read_db_file(item, db)
    except NotFoundError:
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
        if item.components != []:
            for component in item.components:
                [create_new_component(i, refreshed) for i in item.components]
    finally:
        db.close()
    return new_entry


## function to read from the table
def read_db_file(item: CMSContentFile, session: Session) -> CMSContentFile:
    db_file = (
        session.query(TblCMSContentFiles)
        .filter(TblCMSContentFiles.id == item.id)
        .first()
    )
    if db_file is None:
        raise NotFoundError(f"FileId: {item.id} not found")
    return db_file


## function to update the table
def update_entry():
    pass


## function to delete from the table
def delete_entry():
    pass
