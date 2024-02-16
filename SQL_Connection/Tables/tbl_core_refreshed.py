from sqlalchemy import DateTime, Uuid
from uuid import UUID, uuid4
from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped, Session
from SQL_Connection.db_connection import Base, get_db
from pydantic import BaseModel

## creating the pydantic BaseModel
class Refreshed(BaseModel):
    id: UUID = uuid4()
    refreshedAt: datetime = datetime.now()

## Using SQLAlchemy2.0 generate Table with association to the correct schema
class Tbl_Core_Refreshed(Base):
    __tablename__ = 'refreshed'
    __table_args__ = {"schema": "core"}

    id: Mapped[uuid4] = mapped_column(Uuid(), primary_key=True, index=True, nullable=False)
    refreshedAt: Mapped[datetime] = mapped_column(DateTime(), default=datetime.now(), index=True, nullable=False)


## function to write to create a new entry item in the table
def create_new_entry(entry: Refreshed, db_session: Session):
    entry = Refreshed(id: uuid4(), refreshedAt: datetime.now())
    db_item = Tbl_Core_Refreshed()


## function to read from the table
def get_last_item():
    pass