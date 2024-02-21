from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel
from sqlalchemy import DateTime, Uuid
from sqlalchemy.orm import Mapped, Session, mapped_column

from SQL_Connection.db_connection import Base, NotFoundError


## creating the pydantic BaseModel
class Refreshed(BaseModel):
    id: UUID = uuid4()
    refreshedAt: datetime = datetime.now()


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class Tbl_Core_Refreshed(Base):
    __tablename__ = "refreshed"
    __table_args__ = {"schema": "core"}

    id: Mapped[uuid4] = mapped_column(
        Uuid(), primary_key=True, index=True, nullable=False
    )
    refreshedAt: Mapped[datetime] = mapped_column(
        DateTime(), default=datetime.now(), index=True, nullable=False
    )


## function to write to create a new entry item in the table
def create_new_refreshed(session: Session) -> Refreshed:
    # pass
    entry = Refreshed()
    new_entry = Tbl_Core_Refreshed(**entry.model_dump())
    session.add(new_entry)
    session.commit()
    session.refresh(new_entry)
    return new_entry


## function to read from the table
def get_last_refreshed(session: Session) -> Refreshed:
    try:
        item = (
            session.query(Tbl_Core_Refreshed)
            .order_by(Tbl_Core_Refreshed.refreshedAt.desc())
            .first()
        )
    except NotFoundError:
        raise NotFoundError("No previous refresh records found")
    return item
