from uuid import UUID, uuid4

from pydantic import BaseModel
from sqlalchemy import ForeignKey, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from SQL_Connection.db_connection import Base


## creating the pydantic BaseModel
class AccGroupMember(BaseModel):
    groupId: UUID
    userId: UUID
    refreshedId: UUID


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
    userId: Mapped[uuid4] = mapped_column(
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
