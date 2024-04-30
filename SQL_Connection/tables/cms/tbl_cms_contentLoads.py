from datetime import datetime
from uuid import UUID  # , uuid4

from pydantic import BaseModel
from sqlalchemy import (
    Boolean,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Table,
    Uuid,
)
from sqlalchemy.orm import Mapped, Session, mapped_column

from APICore.result_models.cms.content_loads import CMSContentLoad, CMSContentLoadBase
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal
from SQL_Connection.tables.cms.tbl_cms_contentDocuments import (
    create_new_content_document,
)


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblCMSContentLoads(Base):
    __tablename__ = "contentLoads"
    __table_args__ = {"schema": "cms"}

    id: Mapped[UUID] = mapped_column(
        Uuid(),
        primary_key=True,
        index=True,
        nullable=False,
    )
    contentId: Mapped[UUID] = mapped_column(
        Uuid(),
        ForeignKey("cms.contents.id"),
        nullable=True,
    )
    searchId: Mapped[UUID] = mapped_column(
        Uuid(),
        # ForeignKey("cms.searches.id"),
        nullable=True,
    )
    documentId: Mapped[UUID] = mapped_column(
        Uuid(),
        ForeignKey("cms.contentDocuments.id"),
        nullable=True,
    )
    loadedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    loadedById: Mapped[UUID] = mapped_column(
        Uuid(),
        ForeignKey("accounts.users.id"),
        nullable=False,
    )
    refreshedId: Mapped[UUID] = mapped_column(
        Uuid(),
        ForeignKey("core.refreshed.id"),
        nullable=False,
    )


## function to write to create a new entry item in the table
def create_new_content_load(
    item: CMSContentLoad,
    refreshed,
    session: Session = None,
) -> CMSContentLoad:
    base_item = CMSContentLoadBase(**item.model_dump(exclude_none=True))
    new_entry = TblCMSContentLoads(
        **base_item.model_dump(exclude_none=True), refreshedId=refreshed.id
    )
    if session is None:
        db = SessionLocal()
        try:
            new_entry = read_db_content_load(item, db)
        except NotFoundError:
            if item.document is not None:
                try:
                    create_new_content_document(item.document, refreshed, db)
                    db.add(new_entry)
                    db.commit()
                    db.refresh(new_entry)
                except Exception as e:
                    db.rollback()
        finally:
            db.close()
    else:
        db = session
        try:
            new_entry = read_db_content_load(item, db)
        except NotFoundError:
            if item.document is not None:
                try:
                    create_new_content_document(item.document, refreshed, db)
                    db.add(new_entry)
                    db.commit()
                    db.refresh(new_entry)
                except Exception as e:
                    db.rollback()

    return new_entry


## function to read item from the table
def read_db_content_load(item: CMSContentLoad, session: Session) -> CMSContentLoad:
    db_item = session.query(TblCMSContentLoads).filter_by(id=item.id).first()
    if db_item is None:
        raise NotFoundError(f"ContentLoadId: {item.id} not found")
    return db_item


## function to update the table
def update_content_load():
    pass


## function to delete an item from the table
def delete_content_load():
    pass
