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

from APICore.result_models.cms.contents import CMSContent, CMSContentBase
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal


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
    displayUnit: Mapped[str] = mapped_column(String(15), nullable=True)
    revitFamilyHostType: Mapped[str] = mapped_column(String(20), nullable=True)
    refreshedId: Mapped[UUID] = mapped_column(
        ForeignKey("core.refreshed.id"), nullable=False
    )


## function to write to create a new entry item in the table
def create_new_content(item: CMSContent, refreshed) -> CMSContent:
    base_content = CMSContentBase(**item.model_dump())
    new_entry = TblCMSContents(
        **base_content.model_dump(exclude_none=True),
        refreshedId=refreshed.id,
    )  # .model_dump())
    db = SessionLocal()
    try:
        new_entry = read_db_content(item, db)
    except NotFoundError:
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
    finally:
        db.close()
    return new_entry


## function to read from the table
def get_all_contents():
    pass


## function to read from the table
def read_db_content(item: CMSContent, session: Session) -> CMSContent:
    db_content = (
        session.query(TblCMSContents).filter(TblCMSContents.id == item.id).first()
    )
    if db_content is None:
        raise NotFoundError(f"ContentId: {item.id} not found")
    return db_content


## function to update the table
def update_content():
    pass


## function to delete from the table
def delete_content():
    pass
