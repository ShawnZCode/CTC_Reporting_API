from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel
from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import Mapped, Session, mapped_column

from APICore.result_models.cms.content_reviews import CMSContentReview
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblCMSContentReviews(Base):
    __tablename__ = "contentReviews"
    __table_args__ = {"schema": "cms"}

    id: Mapped[uuid4] = mapped_column(
        Uuid(),
        primary_key=True,
        index=True,
        nullable=False,
    )
    contentId: Mapped[uuid4] = mapped_column(
        Uuid(),
        ForeignKey("cms.contents.id"),
        nullable=False,
    )
    rating: Mapped[float] = mapped_column(Float(), nullable=False)
    comment: Mapped[str] = mapped_column(String(250), nullable=True)
    addedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    addedById: Mapped[uuid4] = mapped_column(
        Uuid(),
        ForeignKey("accounts.users.id"),
        nullable=False,
    )
    updatedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    updatedById: Mapped[uuid4] = mapped_column(
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
def create_new_review(
    item: CMSContentReview, refreshed, session: Session = None
) -> CMSContentReview:
    base_review = CMSContentReview(**item.model_dump())
    base_review.refreshedId = refreshed.id
    new_entry = TblCMSContentReviews(**base_review.model_dump(exclude_none=True))
    if session is None:
        db = SessionLocal()
        try:
            new_entry = read_db_review(item, db)
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
            new_entry = read_db_review(item, session)
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
def read_db_review(item: CMSContentReview, session: Session) -> TblCMSContentReviews:
    db_item = (
        session.query(TblCMSContentReviews)
        .filter(TblCMSContentReviews.id == item.id)
        .first()
    )
    if db_item is None:
        raise NotFoundError(f"ReviewId: {item.id} not found")
    db_item_dump = {}
    for key, value in db_item.__dict__.items():
        db_item_dump.update({key: value})
    return CMSContentReview(**db_item_dump)


## function to update the table
def update_review():
    pass


## function to delete from the table
def delete_entry():
    pass
