from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel
from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import Mapped, Session, mapped_column

from APICore.result_models.cms.content_libraries import CMSContentLibrary
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal


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
def create_new_content_library(
    item: CMSContentLibrary, refreshed, session: Session = None
) -> CMSContentLibrary:
    base_content_library = CMSContentLibrary(**item.model_dump(exclude_defaults=True))
    base_content_library.refreshedId = refreshed.id
    new_entry = TblCMSContentLibraries(
        **base_content_library.model_dump(exclude_defaults=True)
    )
    if session is None:
        db = SessionLocal()
    try:
        new_entry = read_db_content_library(new_entry, db)
    except NotFoundError:
        try:
            db.add(new_entry)
            db.commit()
            db.refresh(new_entry)
        except:
            pass
    finally:
        db.close()
    return new_entry


## function to read from the table
def read_db_content_library(
    item: CMSContentLibrary, session: Session
) -> CMSContentLibrary:
    db_content_library = (
        session.query(TblCMSContentLibraries)
        .filter(
            TblCMSContentLibraries.libraryId == item.libraryId,
            TblCMSContentLibraries.contentId == item.contentId,
        )
        .first()
    )
    if db_content_library is None:
        raise NotFoundError(
            f"ContentLibrary record with libraryId {item.libraryId} and contentId {item.contentId} not found"
        )
    return db_content_library


## function to update the table
def update_entry():
    pass


## function to delete from the table
def delete_entry():
    pass
