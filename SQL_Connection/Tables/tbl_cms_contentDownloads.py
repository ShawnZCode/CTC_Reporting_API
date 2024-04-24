from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel
from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import Mapped, Session, mapped_column

from APICore.result_models.cms.content_downloads import CMSContentDownload
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal


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
def create_new_download(
    item: CMSContentDownload, refreshed, session: Session = None
) -> CMSContentDownload:
    base_download = CMSContentDownload(**item.model_dump())
    base_download.refreshedId = refreshed.id
    new_entry = TblCMSContentDownloads(**base_download.model_dump(exclude_none=True))
    db = SessionLocal()
    try:
        new_entry = read_db_download(item, db)
    except NotFoundError:
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
    finally:
        db.close()
    return new_entry


## function to read from the table
def read_db_download(
    item: CMSContentDownload, session: Session
) -> TblCMSContentDownloads:
    db_download = (
        session.query(TblCMSContentDownloads)
        .filter(TblCMSContentDownloads.id == item.id)
        .first()
    )
    if db_download is None:
        raise NotFoundError(f"DownloadId: {item.id} not found")
    return db_download


## function to update the table
def update_entry():
    pass


## function to delete from the table
def delete_entry():
    pass
