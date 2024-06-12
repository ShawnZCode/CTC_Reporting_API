from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel
from sqlalchemy import Boolean, DateTime, ForeignKey, String, Uuid
from sqlalchemy.orm import Mapped, Session, mapped_column

from APICore.result_models.accounts.groups import AccGroup, AccGroupBase
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal
from SQL_Connection.tables.accounts.tbl_acc_groupMembers import write_db_group_member
from SQL_Connection.tables.accounts.tbl_acc_groupRoles import write_db_group_role


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblAccGroups(Base):
    __tablename__ = "groups"
    __table_args__ = {"schema": "accounts"}

    id: Mapped[uuid4] = mapped_column(
        Uuid(), primary_key=True, index=True, nullable=False
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=True)
    addedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    addedById: Mapped[uuid4] = mapped_column(
        ForeignKey("accounts.users.id"), nullable=False
    )
    updatedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    updatedById: Mapped[uuid4] = mapped_column(
        ForeignKey("accounts.users.id"), nullable=False
    )
    isDefaultGroup: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    refreshedId: Mapped[uuid4] = mapped_column(
        ForeignKey("core.refreshed.id"), nullable=False
    )


## function to write to create a new entry item in the table
def write_db_group(
    item: AccGroup,
    refreshed,
    session: Session = None,
) -> AccGroup:
    base_item = AccGroupBase(**item.model_dump(exclude_none=True))
    db_item = TblAccGroups(
        **base_item.model_dump(exclude_none=True), refreshedId=refreshed.id
    )
    if session is None:
        db = SessionLocal()
    else:
        db = session
    try:
        read_db_group(item, db)
    except NotFoundError:
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        if item.roleAssignments != []:
            [write_db_group_role(role, refreshed, db) for role in item.groupRoles]
        if item.groupMembers != []:
            [
                write_db_group_member(member, refreshed, db)
                for member in item.groupMembers
            ]
    if session is None:
        db.close()
    return AccGroup(**db_item.__dict__)


## function to read item from the table
def read_db_group(item: AccGroup, session: Session) -> AccGroup:
    db_item = session.query(TblAccGroups).filter(TblAccGroups.id == item.id).first()
    if db_item is None:
        raise NotFoundError(f"GroupId: {item.id} not found")
    return AccGroup(**db_item.__dict__)


## function to update the table
def update_group(item: AccGroup, session: Session) -> AccGroup:
    update_entry = read_db_group(item, session)
    if item.updatedAt.astimezone(None) > update_entry.updatedAt.astimezone(None):
        for key, value in item.model_dump().items():
            if key != "id":
                setattr(update_entry, key, value)
    session.commit()
    session.refresh(update_entry)
    return update_entry


## function to delete from the table
def delete_entry():
    pass
