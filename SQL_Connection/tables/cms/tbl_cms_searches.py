from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel
from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import Mapped, Session, mapped_column

from APICore.result_models.cms.searches import CMSSearch, CMSSearchBase
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblCMSSearches(Base):
    __tablename__ = "searches"
    __table_args__ = {"schema": "cms"}

    id: Mapped[uuid4] = mapped_column(
        Uuid(), primary_key=True, index=True, nullable=False
    )
    savedSearchId: Mapped[uuid4] = mapped_column(
        Uuid(),
        nullable=True,
    )
    # ForeignKey("cms.savedSearches.id"),
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
    searchedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    searchedById: Mapped[uuid4] = mapped_column(
        ForeignKey("accounts.users.id"), nullable=False
    )
    totalExecutionTimeInMs: Mapped[int] = mapped_column(Integer(), nullable=False)
    totalPageCount: Mapped[int] = mapped_column(Integer(), nullable=False)
    pageSize: Mapped[int] = mapped_column(Integer(), nullable=False)
    totalResultCount: Mapped[int] = mapped_column(Integer(), nullable=False)
    # searchId: Mapped[uuid4] = mapped_column(Uuid(), nullable=False)
    # savedSearchName: Mapped[str] = mapped_column(String(100), nullable=True)
    hasExplicitLibraryFilter: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    displayUnits: Mapped[str] = mapped_column(String(100), nullable=True)
    fileVersions: Mapped[str] = mapped_column(String(100), nullable=True)
    refreshedId: Mapped[uuid4] = mapped_column(
        ForeignKey("core.refreshed.id"), nullable=False
    )


## function to write to create a new entry
def create_new_search(item: CMSSearch, refreshed, session: Session = None) -> CMSSearch:
    base_item = CMSSearchBase(**item.model_dump(exclude_defaults=True))
    new_entry = TblCMSSearches(
        **base_item.model_dump(exclude_defaults=True), refreshedId=refreshed.id
    )
    if session is None:
        db = SessionLocal()
    try:
        new_entry = read_db_library(item, db)
    except NotFoundError:
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
    finally:
        db.close()
    return new_entry


## function to read from the table
def read_db_library(item: CMSSearch, session: Session) -> CMSSearch:
    db_item = session.query(TblCMSSearches).filter(TblCMSSearches.id == item.id).first()
    if db_item is None:
        raise NotFoundError(f"SearchId: {item.id} not found")
    db_item_dump = {}
    for key, value in db_item.__dict__.items():
        db_item_dump.update({key: value})
    return CMSSearch(**db_item_dump)
