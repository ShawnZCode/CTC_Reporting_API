from typing import Optional
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey, Integer, Uuid
from sqlalchemy.orm import Mapped, Session, mapped_column

from APICore.result_models.accounts.groups import AccGroupRole
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblAccGroupRoles(Base):
    __tablename__ = "groupRoles"
    __table_args__ = {"schema": "accounts"}

    groupId: Mapped[uuid4] = mapped_column(
        Uuid(),
        ForeignKey("accounts.groups.id"),
        primary_key=True,
        index=True,
        nullable=False,
    )
    roleId: Mapped[int] = mapped_column(
        Integer(),
        ForeignKey("accounts.roles.id"),
        primary_key=True,
        index=True,
        nullable=False,
    )
    refreshedId: Mapped[uuid4] = mapped_column(
        ForeignKey("core.refreshed.id"), nullable=False
    )


## function to write to create a new entry item in the table
def create_new_group_role(
    item: AccGroupRole, refreshed, session: Session
) -> AccGroupRole:
    new_entry = TblAccGroupRoles(
        groupId=item.groupId, roleId=item.roleId, refreshedId=refreshed.id
    )
    if session is None:
        db = SessionLocal()
        try:
            new_entry = read_db_group_role(item, db)
        except NotFoundError:
            db.add(new_entry)
            db.commit()
            db.refresh(new_entry)
        finally:
            db.close()
    else:
        try:
            new_entry = read_db_group_role(item, session)
        except NotFoundError:
            session.add(new_entry)
            session.commit()
            session.refresh(new_entry)
    return new_entry


## function to read from the table
def read_db_group_role(item: AccGroupRole, session: Session) -> AccGroupRole:
    db_item = (
        session.query(TblAccGroupRoles)
        .filter(
            TblAccGroupRoles.groupId == item.groupId,
            TblAccGroupRoles.roleId == item.roleId,
        )
        .first()
    )
    if db_item is None:
        raise NotFoundError(
            f"GroupId: {item.groupId} + RoleId: {item.roleId} not found"
        )
    db_item_dump = {}
    for key, value in db_item.__dict__.items():
        db_item_dump.update({key: value})
    return AccGroupRole(**db_item_dump)


## function to update the table
def update_entry():
    pass


## function to delete from the table
def delete_entry():
    pass
