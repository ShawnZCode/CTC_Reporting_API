from datetime import datetime
from typing import List, Optional
from uuid import UUID  # , uuid4

from pydantic import BaseModel
from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import Mapped, Session, mapped_column
from tbl_cms_categories import CMSCategory
from tbl_cms_contentAttachments import CMSContentAttachment
from tbl_cms_contentDownloads import CMSContentDownload
from tbl_cms_contentFiles import CMSContentFile
from tbl_cms_contentLoads import CMSContentLoad
from tbl_cms_contentReviews import CMSContentReview
from tbl_cms_contentRevisions import CMSContentRevision
from tbl_cms_libraries import CMSLibrary
from tbl_cms_tags import CMSTag

from SQL_Connection.db_connection import Base


## creating the pydantic BaseModel
class CMSContentBase(BaseModel):
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
    displayUnit: Optional[str] = None
    revitFamilyHostType: Optional[str] = None
    refreshedId: UUID


class CMSContent(CMSContentBase):
    category: Optional[CMSCategory] = None
    contentfiles: Optional[CMSContentFile] = None
    contentAttachments: Optional[List[CMSContentAttachment]] = None
    contentDownlaods: Optional[List[CMSContentDownload]] = None
    contentLoads: Optional[List[CMSContentLoad]] = None
    contentReviews: Optional[List[CMSContentReview]] = None
    contentRevisions: Optional[List[CMSContentRevision]] = None
    contentTags: Optional[List[CMSTag]] = None
    contentLibrary: Optional[List[CMSLibrary]] = None


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblCMSContents(Base):
    __tablename__ = "contents"
    __table_args__ = {"schema": "cms"}

    id: Mapped[UUID] = mapped_column(
        Uuid(), primary_key=True, index=True, nullable=False
    )
    addedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    addedById: Mapped[UUID] = mapped_column(
        ForeignKey("accounts.users.id"), nullable=False
    )
    updatedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    updatedById: Mapped[UUID] = mapped_column(
        ForeignKey("accounts.users.id"), nullable=False
    )
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    fileName: Mapped[str] = mapped_column(String(150), nullable=False)
    fileExtension: Mapped[str] = mapped_column(String(13), nullable=False)
    hasCustomPreviewImage: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    type: Mapped[str] = mapped_column(String(30), nullable=False)
    source: Mapped[str] = mapped_column(String(30), nullable=False)
    location: Mapped[str] = mapped_column(String(20), nullable=False)
    averageRating: Mapped[float] = mapped_column(Float(), nullable=False)
    categoryId: Mapped[int] = mapped_column(
        ForeignKey("cms.categories.id"), nullable=True
    )
    previewImageUri: Mapped[str] = mapped_column(String(2048), nullable=True)
    displayUnit: Mapped[str] = mapped_column(String(10), nullable=True)
    revitFamilyHostType: Mapped[str] = mapped_column(String(20), nullable=True)
    # refreshedId: Mapped[UUID] = mapped_column(
    #    ForeignKey("core.refreshed.id"), nullable=False
    # )


## function to write to create a new entry item in the table
def create_new_content(item: CMSContent, session: Session) -> CMSContent:
    new_entry = TblCMSContents(**item)  # .model_dump())
    session.add(new_entry)
    session.commit()
    session.refresh(new_entry)
    return new_entry


## function to read from the table
def get_all_contents():
    pass


## function to read from the table
def get_content():
    pass


## function to update the table
def update_content():
    pass


## function to delete from the table
def delete_content():
    pass
