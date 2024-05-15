from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

# from fastapi.params import Depends
from sqlalchemy import Boolean, DateTime, ForeignKey, String, Uuid
from sqlalchemy.orm import Mapped, Session, mapped_column

from APICore.result_models.accounts.users_org import AccUser, AccUserBase
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal, get_db
from SQL_Connection.tables.accounts.tbl_acc_userRoles import write_db_user_role


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblAccUsers(Base):
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
    addedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    addedById: Mapped[uuid4] = mapped_column(Uuid(), nullable=False)
    updatedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    updatedById: Mapped[uuid4] = mapped_column(Uuid(), nullable=False)
    isSSOUser: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    refreshedId: Mapped[uuid4] = mapped_column(
        ForeignKey("core.refreshed.id"), nullable=False
    )


## function to write to create a new entry item in the table
def write_db_user(
    item: AccUser,
    refreshed,
    session: Session = None,
) -> AccUser:
    base_user = AccUserBase(**item.model_dump(exclude_none=True))
    if base_user.refreshedId is None:
        base_user.refreshedId = refreshed.id
    if session is None:
        db = SessionLocal()
    else:
        db = session
    db_item = TblAccUsers(**base_user.model_dump())
    try:
        read_db_user(item, db)
    except NotFoundError:
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        if item.roleAssignments != []:
            [write_db_user_role(role, refreshed, db) for role in item.userRoles]
    if session is None:
        db.close()
    return AccUser(**db_item.__dict__)


## function to read from the table
def get_all_users():
    pass


## function to read item from the table
def read_db_user(item: AccUser, session: Session = None) -> AccUser:
    if session is None:
        db = SessionLocal()
    else:
        db = session
    db_item = db.query(TblAccUsers).filter(TblAccUsers.id == item.id).first()
    if db_item is None:
        raise NotFoundError(f"UserId: {item.id} not found")
    if session is None:
        db.close()
    return AccUser(**db_item.__dict__)


## function to update the table
def update_user(item: AccUser, session: Session) -> AccUser:
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
