from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel
from sqlalchemy import ForeignKey, Integer, Uuid
from sqlalchemy.orm import Mapped, Session, mapped_column

from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal


## creating the pydantic BaseModel
class AccUserRole(BaseModel):
    userId: UUID
    roleId: int
    refreshedId: Optional[UUID] = None


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblAccUserRoles(Base):
    __tablename__ = "userRoles"
    __table_args__ = {"schema": "accounts"}

    userId: Mapped[uuid4] = mapped_column(
        Uuid(),
        ForeignKey("accounts.users.id"),
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
def write_db_user_role(
    item: AccUserRole,
    refreshed,
    session: Session = None,
) -> AccUserRole:
    db_item = TblAccUserRoles(
        **item.model_dump(exclude_none=True), refreshedId=refreshed.id
    )
    if session is None:
        db = SessionLocal()
    else:
        db = session
    try:
        read_db_user_role(item, db)
    except NotFoundError:
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
    if session is None:
        db.close()
    return AccUserRole(**db_item.__dict__)


## function to read from the table
def read_db_user_role(item: AccUserRole, session: Session = None) -> AccUserRole:
    if session is None:
        db = SessionLocal()
    else:
        db = session
    try:
        db_item = (
            db.query(TblAccUserRoles)
            .filter(
                TblAccUserRoles.userId == item.userId,
                TblAccUserRoles.roleId == item.roleId,
            )
            .first()
        )
    except NotFoundError:
        raise NotFoundError(
            f"UserId: {item.userId} with RoleId: {item.roleId} not found"
        )
    if session is None:
        db.close()
    return AccUserRole(**db_item.__dict__)


## function to update the table
def update_entry():
    pass


## function to delete from the table
def delete_entry():
    pass
