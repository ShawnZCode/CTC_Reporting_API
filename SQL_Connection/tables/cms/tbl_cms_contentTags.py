from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from sqlalchemy import (
    Boolean,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Uuid,
)
from sqlalchemy.orm import Mapped, Session, mapped_column

from APICore.result_models.cms.content_tags import CMSContentTag
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblCMSContentTags(Base):
    __tablename__ = "contentTags"
    __table_args__ = {"schema": "cms"}

    contentId: Mapped[uuid4] = mapped_column(
        ForeignKey("cms.contents.id"), primary_key=True, index=True, nullable=False
    )
    tagId: Mapped[uuid4] = mapped_column(
        ForeignKey("cms.tags.id"), primary_key=True, index=True, nullable=False
    )
    refreshedId: Mapped[uuid4] = mapped_column(
        ForeignKey("core.refreshed.id"), nullable=False
    )


## function to write to create a new entry item in the table
def create_new_content_tag(
    item: CMSContentTag, refreshed, session: Session = None
) -> CMSContentTag:
    base_content_tag = CMSContentTag(**item.model_dump(exclude_defaults=True))
    base_content_tag.refreshedId = refreshed.id
    new_entry = TblCMSContentTags(**base_content_tag.model_dump(exclude_defaults=True))
    if session is None:
        db = SessionLocal()
    try:
        new_entry = read_db_content_tag(new_entry, db)
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
def read_db_content_tag(item: CMSContentTag, session: Session) -> CMSContentTag:
    db_item = (
        session.query(TblCMSContentTags)
        .filter(
            TblCMSContentTags.contentId == item.contentId,
            TblCMSContentTags.tagId == item.tagId,
        )
        .first()
    )
    if db_item is None:
        raise NotFoundError(
            f"ContentId: {item.contentId} + TagId: {item.tagId} not found"
        )
    db_item_dump = {}
    for key, value in db_item.__dict__.items():
        db_item_dump.update({key: value})
    return CMSContentTag(**db_item_dump)
