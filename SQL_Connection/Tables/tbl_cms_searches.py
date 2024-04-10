from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel
from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from SQL_Connection.db_connection import Base


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblCMSSearches(Base):
    __tablename__ = "searches"
    __table_args__ = {"schema": "cms"}

    id: Mapped[uuid4] = mapped_column(
        Uuid(), primary_key=True, index=True, nullable=False
    )
    savedSearchId: Mapped[uuid4] = mapped_column(
        ForeignKey("cms.savedSearches.id"), nullable=True
    )
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
    executionTimeInMs: Mapped[int] = mapped_column(Integer(), nullable=False)
    page: Mapped[int] = mapped_column(Integer(), nullable=False)
    pageSize: Mapped[int] = mapped_column(Integer(), nullable=False)
    searchId: Mapped[uuid4] = mapped_column(Uuid(), nullable=False)
    resultCount: Mapped[int] = mapped_column(Integer(), nullable=False)
    savedSearchName: Mapped[str] = mapped_column(String(100), nullable=True)
    hasExplicitLibraryFilter: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    displayUnits: Mapped[str] = mapped_column(String(100), nullable=True)
    fileVersions: Mapped[str] = mapped_column(String(100), nullable=True)
    refreshedId: Mapped[uuid4] = mapped_column(
        ForeignKey("core.refreshed.id"), nullable=False
    )


## function to write to create a new entry
def create_new_entry():
    pass


## function to read from the table
def get_all_items():
    pass


## function to update the table
def update_entry():
    pass


## function to delete from the table
def delete_entry():
    pass
