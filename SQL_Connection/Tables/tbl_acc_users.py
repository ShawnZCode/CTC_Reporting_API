from sqlalchemy import DateTime, Uuid, String, Boolean, Float, Integer, ForeignKey
from uuid import UUID, uuid4
from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped
from SQL_Connection.db_connection import Base
from pydantic import BaseModel
from typing import Optional


## creating the 'users' pydantic BaseModel
class Acc_Users(BaseModel):
    id: UUID
    firstName: str
    lastName: str
    displayName: str
    description: Optional[str]
    office: Optional[str]
    department: Optional[str]
    lastLoggedInAt: datetime
    status: str
    createdAt: datetime
    createdBtId: UUID
    updatedAt: datetime
    updatedById: UUID
    isSSOUser: bool
    refreshedId: UUID

## Using SQLAlchemy2.0 generate 'users' Table Creation with association to the 'accounts' schema
class Tbl_Acc_Users(Base):
    __tablename__ = 'users'
    __table_args__ = {"schema": "accounts"}

    id: Mapped[uuid4] = mapped_column(Uuid(), primary_key=True, index=True, nullable=False)
    firstName: Mapped[str] = mapped_column(String(100), nullable=False)
    lastName: Mapped[str] = mapped_column(String(100), nullable=False)
    displayName: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=True)
    office: Mapped[str] = mapped_column(String(100), nullable=True)
    department: Mapped[str] = mapped_column(String(100), nullable=True)
    lastLoggedInAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False)
    createdAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    createdBtId: Mapped[uuid4] = mapped_column(Uuid(), nullable=False)
    updatedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    updatedById: Mapped[uuid4] = mapped_column(Uuid(), nullable=False)
    isSSOUser: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    refreshedId: Mapped[uuid4] = mapped_column(ForeignKey('core.refreshed.id'), nullable=False)

## function to write to create a new entry item in the contents table
def create_new_user_entry():
    pass

## function to read from the contents table
def get_all_users():
    pass

## function to update the contents table
def update_user_entry():
    pass

## function to delete from the contents table
def delete_user_entry():
    pass
