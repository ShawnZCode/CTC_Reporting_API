from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel
from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import Mapped, Session, mapped_column

from APICore.result_models.cms.content_file_component_properties import (
    CMSContentFileComponentProperty,
)
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblCMSContentFileComponentProperties(Base):
    __tablename__ = "contentFileComponentProperties"
    __table_args__ = {"schema": "cms"}

    id: Mapped[uuid4] = mapped_column(
        Uuid(), primary_key=True, index=True, nullable=False
    )
    contentFileComponentId: Mapped[uuid4] = mapped_column(
        ForeignKey("cms.contentFileComponents.id"), nullable=False
    )
    isInstance: Mapped[bool] = mapped_column(Boolean(), nullable=True)
    isReadOnly: Mapped[bool] = mapped_column(Boolean(), nullable=True)
    name: Mapped[str] = mapped_column(String(2048), nullable=True)
    revitParameterGroupId: Mapped[int] = mapped_column(Integer(), nullable=True)
    revitSharedParameterGuid: Mapped[uuid4] = mapped_column(Uuid(), nullable=True)
    revitStorageTypeId: Mapped[int] = mapped_column(Integer(), nullable=True)
    revitDisplayUnitTypeId: Mapped[int] = mapped_column(Integer(), nullable=True)
    doubleValue: Mapped[float] = mapped_column(Float(), nullable=True)
    type: Mapped[str] = mapped_column(String(100), nullable=True)
    value: Mapped[str] = mapped_column(String(2048), nullable=True)
    unitTypeIdVersionless: Mapped[str] = mapped_column(String(2048), nullable=True)
    refreshedId: Mapped[uuid4] = mapped_column(
        ForeignKey("core.refreshed.id"), nullable=False
    )


## function to write to create a new entry item in the table
def create_new_property(
    item: CMSContentFileComponentProperty,
    refreshed,
    session: Session = None,
) -> CMSContentFileComponentProperty:
    base_property = CMSContentFileComponentProperty(**item.model_dump())
    base_property.refreshedId = refreshed.id
    new_entry = TblCMSContentFileComponentProperties(
        **base_property.model_dump(),
    )
    db = SessionLocal()
    try:
        new_entry = read_db_property(item, db)
    except NotFoundError:
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
    finally:
        db.close()
    return new_entry


## function to read from the table
def read_db_property(
    item: CMSContentFileComponentProperty, session: Session
) -> CMSContentFileComponentProperty:
    db_item = (
        session.query(TblCMSContentFileComponentProperties)
        .filter(TblCMSContentFileComponentProperties.id == item.id)
        .first()
    )
    if db_item is None:
        raise NotFoundError(f"PropertyId: {item.id} not found")
    db_item_dump = {}
    for key, value in db_item.__dict__.items():
        db_item_dump.update({key: value})
    return CMSContentFileComponentProperty(**db_item_dump)


## function to update the table
def update_entry():
    pass


## function to delete from the table
def delete_entry():
    pass
