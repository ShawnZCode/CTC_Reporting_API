from uuid import UUID, uuid4

from sqlalchemy import ForeignKey, Uuid
from sqlalchemy.orm import Mapped, Session, mapped_column

from APICore.result_models.accounts.groups import AccGroupMember
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblAccGroupMembers(Base):
    __tablename__ = "groupMembers"
    __table_args__ = {"schema": "accounts"}

    groupId: Mapped[uuid4] = mapped_column(
        Uuid(),
        ForeignKey("accounts.groups.id"),
        primary_key=True,
        index=True,
        nullable=False,
    )
    memberId: Mapped[uuid4] = mapped_column(
        Uuid(),
        ForeignKey("accounts.users.id"),
        primary_key=True,
        index=True,
        nullable=False,
    )
    refreshedId: Mapped[uuid4] = mapped_column(
        ForeignKey("core.refreshed.id"), nullable=False
    )


## function to write to create a new entry item in the table
def create_new_group_member(
    item: AccGroupMember, refreshed, session: Session
) -> AccGroupMember:
    new_entry = TblAccGroupMembers(
        groupId=item.groupId, memberId=item.memberId, refreshedId=refreshed.id
    )
    if session is None:
        db = SessionLocal()
        try:
            new_entry = read_db_group_member(item, db)
        except NotFoundError:
            try:
                db.add(new_entry)
                db.commit()
                db.refresh(new_entry)
            except Exception as e:
                db.rollback()
                return e
        finally:
            db.close()
    else:
        try:
            new_entry = read_db_group_member(item, session)
        except NotFoundError:
            try:
                session.add(new_entry)
                session.commit()
                session.refresh(new_entry)
            except Exception as e:
                session.rollback()
                return e
    return new_entry


## function to read from the table
def read_db_group_member(item: AccGroupMember, session: Session) -> AccGroupMember:
    db_group_member = (
        session.query(TblAccGroupMembers)
        .filter(
            TblAccGroupMembers.groupId == item.groupId,
            TblAccGroupMembers.memberId == item.memberId,
        )
        .first()
    )
    if db_group_member is None:
        raise NotFoundError(
            f"GroupId: {item.groupId} with MemberId: {item.memberId} not found"
        )
    return db_group_member


## function to update the table
def update_entry():
    pass


## function to delete from the table
def delete_entry():
    pass
