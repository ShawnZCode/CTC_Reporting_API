from sqlalchemy import DateTime, Uuid, String, Boolean, Float, Integer, ForeignKey
from uuid import UUID, uuid4
from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped
from SQL_Connection.db_connection import Base
from pydantic import BaseModel
from typing import Optional

## creating the pydantic BaseModel
class CMS_ContentFileComponentProperties(BaseModel):
    id: UUID
    contentFileComponentId: UUID
    isinstance: bool
    isReadOnly: bool
    name: str
    revirParameterGroupId: int
    revitSharedParameterGuid: UUID
    revitStorageTypeId: int
    revitDisplayUnitTypeId: int
    doubleValue: float
    type: int
    value: str
    unitTypeIdVersionless: str
    refreshedId: UUID

## Using SQLAlchemy2.0 generate Table with association to the correct schema
class Tbl_CMS_ContentFileComponentProperties(Base):
    __tablename__ = 'contentFileComponentProperties'
    __table_args__ = {"schema": "cms"}

    id: Mapped[uuid4] = mapped_column(Uuid(), primary_key=True, index=True, nullable=False)
    contentFileComponentId: Mapped[uuid4] = mapped_column(ForeignKey('cms.contentFileComponents.id'), nullable=False)
    isinstance: Mapped[bool] = mapped_column(Boolean(), nullable=True)
    isReadOnly: Mapped[bool] = mapped_column(Boolean(), nullable=True)
    name: Mapped[str] = mapped_column(String(2048), nullable=True)
    revirParameterGroupId: Mapped[int] = mapped_column(Integer(), nullable=True)
    revitSharedParameterGuid: Mapped[uuid4] = mapped_column(Uuid(), nullable=True)
    revitStorageTypeId: Mapped[int] = mapped_column(Integer(), nullable=True)
    revitDisplayUnitTypeId: Mapped[int] = mapped_column(Integer(), nullable=True)
    doubleValue: Mapped[float] = mapped_column(Float(), nullable=True)
    type: Mapped[int] = mapped_column(Integer(), nullable=False)
    value: Mapped[str] = mapped_column(String(2048), nullable=True)
    unitTypeIdVersionless: Mapped[str] = mapped_column(String(2048), nullable=True)
    refreshedId: Mapped[uuid4] = mapped_column(ForeignKey('core.refreshed.id'), nullable=False)

    ## function to write to create a new entry item in the table
    def create_new_entry():
        pass

    ## function to read from the table
    def read_entry():
        pass

    ## function to update the table
    def update_entry():
        pass

    ## function to delete from the table
    def delete_entry():
        pass