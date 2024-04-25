from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel
from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import Mapped, Session, mapped_column

from APICore.result_models.cms.saved_searches import CMSSavedSearch, CMSSavedSearchBase
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal


## creating the pydantic BaseModel
class CMSSavedSearch(BaseModel):
    id: UUID
    addedAt: datetime
    addedById: UUID
    updatedAt: datetime
    updatedById: UUID
    name: str
    scope: str
    description: str
    query: str
    sortBy: str
    sortDirection: str
    minAvgRating: int
    addedStartDate: datetime
    addedEndDate: datetime
    addedByUser: str
    updatedStartDate: datetime
    updatedEndDate: datetime
    updatedByUser: str
    displayUnits: str
    fileVersions: str
    filterContentByNotTagged: bool
    fileExtensions: str
    revitRAmilyHostTypes: str
    refreshedId: UUID


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblCMSSavedSearches(Base):
    __tablename__ = "savedSearches"
    __table_args__ = {"schema": "cms"}

    id: Mapped[uuid4] = mapped_column(
        Uuid(), primary_key=True, index=True, nullable=False
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
    scope: Mapped[str] = mapped_column(String(20), nullable=False)
    description: Mapped[str] = mapped_column(String(2048), nullable=True)
    query: Mapped[str] = mapped_column(String(100), nullable=True)
    sortBy: Mapped[str] = mapped_column(String(10), nullable=False)
    sortDirection: Mapped[str] = mapped_column(String(10), nullable=False)
    minAvgRating: Mapped[int] = mapped_column(Integer(), nullable=True)
    addedStartDate: Mapped[datetime] = mapped_column(DateTime(), nullable=True)
    addedEndDate: Mapped[datetime] = mapped_column(DateTime(), nullable=True)
    addedByUser: Mapped[str] = mapped_column(String(2048), nullable=True)
    updatedStartDate: Mapped[datetime] = mapped_column(DateTime(), nullable=True)
    updatedEndDate: Mapped[datetime] = mapped_column(DateTime(), nullable=True)
    updatedByUser: Mapped[str] = mapped_column(String(2048), nullable=True)
    displayUnits: Mapped[str] = mapped_column(String(100), nullable=True)
    fileVersions: Mapped[str] = mapped_column(String(100), nullable=True)
    filterContentByNotTagged: Mapped[bool] = mapped_column(Boolean(), nullable=True)
    fileExtensions: Mapped[str] = mapped_column(String(100), nullable=True)
    revitFamilyHostTypes: Mapped[str] = mapped_column(String(13), nullable=True)
    refreshedId: Mapped[uuid4] = mapped_column(
        ForeignKey("core.refreshed.id"), nullable=False
    )


## function to write to create a new entry
def create_new_saved_search(
    item: CMSSavedSearch, refreshed, session: Session = None
) -> CMSSavedSearch:
    base_item = CMSSavedSearchBase(**item.model_dump(exclude_defaults=True))
    new_entry = TblCMSSavedSearches(
        **base_item.model_dump(exclude_defaults=True), refreshedId=refreshed.id
    )
    if session is None:
        db = SessionLocal()
    try:
        new_entry = read_db_saved_search(item, db)
    except NotFoundError:
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
    finally:
        db.close()
    return new_entry


## function to read from the table
def read_db_saved_search(item: CMSSavedSearch, session: Session) -> CMSSavedSearch:
    db_item = (
        session.query(TblCMSSavedSearches)
        .filter(TblCMSSavedSearches.id == item.id)
        .first()
    )
    if db_item is None:
        raise NotFoundError(f"SavedSearchId: {item.id} not found")
    return db_item


## function to update the table
def update_entry():
    pass


## function to delete from the table
def delete_entry():
    pass
