from sqlalchemy import DateTime, Uuid
from sqlalchemy.orm import mapped_column, Mapped
from SQL_Connection.db_connection import Base

## Using SQLAlchemy2.0 generate 'refreshed' Table Creation with association to the 'cms' schema
class Tbl_Core_Refreshed(Base):
    __tablename__ = 'refreshed'
    __table_args__ = {"schema": "core"}

    id: Mapped[Uuid] = mapped_column(primary_key=True, index=True)
    refreshedat: Mapped[DateTime]

## methods to write to create a new entry item in the refreshed table
def create_new_refreshed_entry():
    pass

## methods to read from the table
def get_last_from_refreshed():
    pass