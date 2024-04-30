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

from APICore.result_models.cms.content_document import CMSContentDocument
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblCMSContentDocuments(Base):
    __tablename__ = "contentDocuments"
    __table_args__ = {"schema": "cms"}

    id: Mapped[UUID] = mapped_column(
        Uuid(), primary_key=True, index=True, nullable=False
    )
    fileName: Mapped[str] = mapped_column(String(150), nullable=False)
    filePath: Mapped[str] = mapped_column(String(2048), nullable=False)
    type: Mapped[str] = mapped_column(String(30), nullable=False)
    version: Mapped[str] = mapped_column(String(30), nullable=False)
    revitCentralModelFilePath: Mapped[str] = mapped_column(String(2048), nullable=True)
    revitWorksharingMode: Mapped[str] = mapped_column(String(30), nullable=True)
    refreshedId: Mapped[UUID] = mapped_column(
        ForeignKey("core.refreshed.id"), nullable=True
    )


## function to write to create a new entry item in the table
def create_new_content_document(
    item: CMSContentDocument,
    refreshed,
    session: Session,
) -> CMSContentDocument:
    base_item = CMSContentDocument(**item.model_dump(exclude_none=True))
    new_entry = TblCMSContentDocuments(
        **base_item.model_dump(exclude_none=True), refreshedId=refreshed.id
    )
    if session is None:
        db = SessionLocal()
        try:
            new_entry = read_db_content_document(item, db)
        except NotFoundError:
            db.add(new_entry)
            db.commit()
            db.refresh(new_entry)
        finally:
            db.close()
    else:
        try:
            new_entry = read_db_content_document(item, session)
        except NotFoundError:
            session.add(new_entry)
            session.commit()
            session.refresh(new_entry)
    return new_entry


## function to read item from the table
def read_db_content_document(
    item: CMSContentDocument, session: Session
) -> CMSContentDocument:
    db_item = session.query(TblCMSContentDocuments).filter_by(id=item.id).first()
    if db_item is None:
        raise NotFoundError(f"DocumentId: {item.id} not found")
    return db_item


## function to update the table
def update_content_document():
    pass


## function to delete an item from the table
def delete_content_document():
    pass
