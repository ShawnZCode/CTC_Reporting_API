from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

# from fastapi.params import Depends
from pydantic import BaseModel
from sqlalchemy import Boolean, DateTime, ForeignKey, String, Uuid
from sqlalchemy.orm import Mapped, Session, mapped_column

from SQL_Connection.db_connection import Base, NotFoundError


## creating the pydantic BaseModel
class Acc_UserRecord(BaseModel):
    id: UUID
    firstName: Optional[str]
    lastName: Optional[str]
    displayName: Optional[str]
    email: str
    description: Optional[str]
    office: Optional[str]
    department: Optional[str]
    lastLoggedInAt: Optional[datetime]
    status: str
    createdAt: datetime
    createdById: UUID
    updatedAt: datetime
    updatedById: UUID
    isSSOUser: bool
    roles: Optional[list[int]]
    # refreshedId: UUID


class Acc_User(BaseModel):
    id: UUID
    firstName: Optional[str]
    lastName: Optional[str]
    displayName: Optional[str]
    email: str
    description: Optional[str]
    office: Optional[str]
    department: Optional[str]
    lastLoggedInAt: Optional[datetime]
    status: str
    createdAt: datetime
    createdById: UUID
    updatedAt: datetime
    updatedById: UUID
    isSSOUser: bool


class Acc_User_Updated(BaseModel):
    id: UUID
    updatedAt: datetime


class Acc_UserRoles(BaseModel):
    id: UUID
    roles: Optional[list[int]]


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class Tbl_Acc_Users(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "accounts"}

    id: Mapped[uuid4] = mapped_column(
        Uuid(), primary_key=True, index=True, nullable=False
    )
    firstName: Mapped[str] = mapped_column(String(100), nullable=True)
    lastName: Mapped[str] = mapped_column(String(100), nullable=True)
    displayName: Mapped[str] = mapped_column(String(100), nullable=True)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=True)
    office: Mapped[str] = mapped_column(String(100), nullable=True)
    department: Mapped[str] = mapped_column(String(100), nullable=True)
    lastLoggedInAt: Mapped[datetime] = mapped_column(DateTime(), nullable=True)
    status: Mapped[str] = mapped_column(String(20), nullable=False)
    createdAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    createdById: Mapped[uuid4] = mapped_column(Uuid(), nullable=False)
    updatedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    updatedById: Mapped[uuid4] = mapped_column(Uuid(), nullable=False)
    isSSOUser: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    # refreshedId: Mapped[uuid4] = mapped_column(ForeignKey('core.refreshed.id'), nullable=False)


## function to write to create a new entry item in the table
def create_new_user(item: Acc_User, session: Session) -> Acc_User:
    new_entry = Tbl_Acc_Users(**item.model_dump())
    session.add(new_entry)
    session.commit()
    session.refresh(new_entry)
    return new_entry


## function to read from the table
def get_all_users():
    pass


## function to read item from the table
def read_db_user(item: Acc_User, session: Session) -> Acc_User:
    db_user = session.query(Tbl_Acc_Users).filter(Tbl_Acc_Users.id == item.id).first()
    if db_user is None:
        raise NotFoundError(f"UserId: {item.id} not found")
    return db_user


## function to update the table
def update_user(item: Acc_User, session: Session) -> Acc_User:
    update_entry = read_db_user(item, session)
    if item.updatedAt.astimezone(None) > update_entry.updatedAt.astimezone(None):
        for key, value in item.model_dump().items():
            if key != "id":
                setattr(update_entry, key, value)
    session.commit()
    session.refresh(update_entry)
    return update_entry


## function to delete from the table
def delete_user():
    pass
