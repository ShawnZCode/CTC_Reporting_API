from sqlalchemy import DateTime, Uuid
from uuid import UUID, uuid4
from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped
from SQL_Connection.db_connection import Base
from pydantic import BaseModel

## creating the 'refreshed' pydantic BaseModel
class Refreshed(BaseModel):
    id: UUID = uuid4()
    refreshedAt: datetime = datetime.now()

## Using SQLAlchemy2.0 generate 'refreshed' Table Creation with association to the 'cms' schema
class Tbl_Core_Refreshed(Base):
    __tablename__ = 'refreshed'
    __table_args__ = {"schema": "core"}

    id: Mapped[uuid4] = mapped_column(Uuid(), primary_key=True, index=True, nullable=False)
    refreshedAt: Mapped[datetime] = mapped_column(DateTime(), default=datetime.now(), index=True, nullable=False)

## methods to write to create a new entry item in the refreshed table
def create_new_refreshed_entry():
    pass

## methods to read from the table
def get_last_from_refreshed():
    pass