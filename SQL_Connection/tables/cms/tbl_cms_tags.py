from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel
from sqlalchemy import DateTime, ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import Mapped, Session, mapped_column

from APICore.result_models.cms.tags import CMSTag, CMSTagBase
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal
from SQL_Connection.tables.cms.tbl_cms_contentTags import create_new_content_tag


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblCMSTags(Base):
    __tablename__ = "tags"
    __table_args__ = {"schema": "cms"}

    id: Mapped[uuid4] = mapped_column(
        Uuid, primary_key=True, index=True, nullable=False
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
    description: Mapped[str] = mapped_column(String(2048), nullable=True)
    refreshedId: Mapped[uuid4] = mapped_column(
        ForeignKey("core.refreshed.id"), nullable=False
    )


## function to write to create a new entry item in the table
def create_new_tag(item: CMSTag, refreshed) -> CMSTag:
    base_item = CMSTagBase(**item.model_dump(exclude_none=True))
    new_entry = TblCMSTags(
        **base_item.model_dump(exclude_none=True), refreshedId=refreshed.id
    )
    db = SessionLocal()
    try:
        new_entry = get_db_tag(item, db)
    except NotFoundError:
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
        if item.contentTags != []:
            [create_new_content_tag(ct, refreshed) for ct in item.contentTags]
    finally:
        db.close()
    return new_entry


## function to read from the table
def get_db_tag(item: CMSTag, db: Session) -> CMSTag:
    db_item = db.query(TblCMSTags).filter(TblCMSTags.id == item.id).first()
    if db_item is None:
        raise NotFoundError(f"TagId {item.id} not found")
    db_item_dump = {}
    for key, value in db_item.__dict__.items():
        db_item_dump.update({key: value})
    return CMSTag(**db_item_dump)


## function to update the table
def update_entry():
    pass


## function to delete from the table
def delete_entry():
    pass
