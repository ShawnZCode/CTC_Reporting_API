from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel
from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import Mapped, Session, mapped_column

from APICore.result_models.cms.content_revisions import CMSContentRevision
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblCMSContentRevisions(Base):
    __tablename__ = "contentRevisions"
    __table_args__ = {"schema": "cms"}

    id: Mapped[uuid4] = mapped_column(
        Uuid(), primary_key=True, index=True, nullable=False
    )
    contentId: Mapped[uuid4] = mapped_column(
        ForeignKey("cms.contents.id"), nullable=False
    )
    comment: Mapped[str] = mapped_column(String(250), nullable=True)
    revisedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    revisedById: Mapped[uuid4] = mapped_column(
        Uuid(),
        ForeignKey("accounts.users.id"),
        nullable=False,
    )
    refreshedId: Mapped[uuid4] = mapped_column(
        Uuid(),
        ForeignKey("core.refreshed.id"),
        nullable=False,
    )


## function to write to create a new entry item in the table
def create_new_revision(
    item: CMSContentRevision, refreshed, session: Session = None
) -> CMSContentRevision:
    base_revision = CMSContentRevision(**item.model_dump())
    base_revision.refreshedId = refreshed.id
    new_entry = TblCMSContentRevisions(**base_revision.model_dump(exclude_none=True))
    if session is None:
        db = SessionLocal()
        try:
            new_entry = read_db_revision(item, db)
        except NotFoundError:
            try:
                db.add(new_entry)
                db.commit()
                db.refresh(new_entry)
            except Exception as e:
                db.rollback()
                raise e
        finally:
            db.close()
    else:
        try:
            new_entry = read_db_revision(item, session)
        except NotFoundError:
            try:
                session.add(new_entry)
                session.commit()
                session.refresh(new_entry)
            except Exception as e:
                session.rollback()
                raise e
    return new_entry


## function to read from the table
def read_db_revision(
    item: CMSContentRevision, session: Session
) -> TblCMSContentRevisions:
    db_item = (
        session.query(TblCMSContentRevisions)
        .filter(TblCMSContentRevisions.id == item.id)
        .first()
    )
    if db_item is None:
        raise NotFoundError(f"RevisionId: {item.id} not found")
    db_item_dump = {}
    for key, value in db_item.__dict__.items():
        db_item_dump.update({key: value})
    return CMSContentRevision(**db_item_dump)


## function to update the table
def update_revision():
    pass


## function to delete from the table
def delete_entry():
    pass
