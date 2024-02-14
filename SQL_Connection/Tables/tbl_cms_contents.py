from sqlalchemy import DateTime, Uuid, String, Boolean, Float, Integer, ForeignKey
from uuid import UUID, uuid4
from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped
from SQL_Connection.db_connection import Base
from pydantic import BaseModel
from typing import Optional


## creating the 'refreshed' pydantic BaseModel
class CMS_Contents(BaseModel):
    id: UUID
    addedAt: datetime
    addedById: UUID
    updatedAt: datetime
    updatedById: UUID
    name: str
    fileName: str
    fileExtension: str
    hasCustomPreviewImage: bool
    type: str
    source: str
    location: str
    averageRating: float
    categoryId: Optional[int] = None
    previewImageUri: Optional[str] = None
    dispalyUnit: Optional[str] = None
    revitFamilyHostType: Optional[str] = None
    refreshedId: UUID


## Using SQLAlchemy2.0 generate 'refreshed' Table Creation with association to the 'cms' schema
class Tbl_CMS_Contents(Base):
    __tablename__ = 'contents'
    __table_args__ = {"schema": "cms"}

    id: Mapped[uuid4] = mapped_column(Uuid(), primary_key=True, index=True, nullable=False)
    addedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    addedById: Mapped[uuid4] = mapped_column(ForeignKey('accounts.users.id'), nullable=False)
    updatedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    updatedById: Mapped[uuid4] = mapped_column(ForeignKey('accounts.users.id'), nullable=False)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    fileName: Mapped[str] = mapped_column(String(150), nullable=False)
    fileExtension: Mapped[str] = mapped_column(String(13), nullable=False)
    hasCustomPreviewImage: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    type: Mapped[str] = mapped_column(String(30), nullable=False)
    source: Mapped[str] = mapped_column(String(30), nullable=False)
    location: Mapped[str] = mapped_column(String(20), nullable=False)
    averageRating: Mapped[float] = mapped_column(Float(), nullable=False)
    categoryId: Mapped[int] = mapped_column(Integer(), nullable=True)
    previewImageUri: Mapped[str] = mapped_column(String(2048), nullable=True)
    dispalyUnit: Mapped[str] = mapped_column(String(10), nullable=True)
    revitFamilyHostType: Mapped[str] = mapped_column(String(20), nullable=True)
    refreshedId: Mapped[uuid4] = mapped_column(ForeignKey('core.refreshed.id'), nullable=False)



## function to write to create a new entry item in the contents table
def create_new_contents_entry():
    pass

## function to read from the contents table
def get_all_contents():
    pass

## function to update the contents table
def update_contents_entry():
    pass

## function to delete from the contents table
def delete_contents_entry():
    pass
