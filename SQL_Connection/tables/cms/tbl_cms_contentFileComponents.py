from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel
from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import Mapped, Session, mapped_column

from APICore.result_models.cms.content_file_components import (
    CMSContentFileComponent,
    CMSContentFileComponentBase,
)
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal
from SQL_Connection.tables.cms.tbl_cms_contentFileComponentProperties import (
    create_new_property,
)


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblCMSContentFileComponents(Base):
    __tablename__ = "contentFileComponents"
    __table_args__ = {"schema": "cms"}

    id: Mapped[uuid4] = mapped_column(
        Uuid(as_uuid=True), primary_key=True, index=True, nullable=False
    )
    contentFileId: Mapped[uuid4] = mapped_column(
        ForeignKey("cms.contentFiles.id"), index=True, nullable=False
    )
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    refreshedId: Mapped[uuid4] = mapped_column(
        ForeignKey("core.refreshed.id"), nullable=False
    )


## function to write to create a new entry item in the table
def create_new_component(
    item: CMSContentFileComponent, refreshed, session: Session = None
) -> CMSContentFileComponent:
    base_component = CMSContentFileComponentBase(**item.model_dump())
    base_component.refreshedId = refreshed.id
    new_entry = TblCMSContentFileComponents(
        **base_component.model_dump(),
    )
    db = SessionLocal()
    try:
        new_entry = read_db_component(item, db)
    except NotFoundError:
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
        if item.properties != []:
            [create_new_property(prop, refreshed) for prop in item.properties]
    finally:
        db.close()
    return new_entry


## function to read from the table
def read_db_component(
    item: CMSContentFileComponent,
    session: Session = None,
) -> CMSContentFileComponent:
    db_item = (
        session.query(TblCMSContentFileComponents)
        .filter(TblCMSContentFileComponents.id == item.id)
        .first()
    )
    if db_item is None:
        raise NotFoundError(f"ComponentId: {item.id} not found")
    db_item_dump = {}
    for key, value in db_item.__dict__.items():
        db_item_dump.update({key: value})
    return CMSContentFileComponent(**db_item_dump)


## function to update the table
def update_entry():
    pass


## function to delete from the table
def delete_entry():
    pass
