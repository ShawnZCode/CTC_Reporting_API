from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column, Mapped
from SQL_Connection.db_connection import Base
from pydantic import BaseModel


## creating the pydantic BaseModel
class Acc_Roles(BaseModel):
    id: int
    dispalyName: str

## Using SQLAlchemy2.0 generate Table with association to the correct schema
class Tbl_Acc_Roles(Base):
    __tablename__ = 'roles'
    __table_args__ = {"schema": "accounts"}

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, index=True, nullable=False)
    displayName: Mapped[str] = mapped_column(String(100), nullable=False)

    ## initialize the table
    def __init__(self, id: int, displayName: str):
        self.id = id
        self.displayName = displayName

    ## function to write to create a new entry item in the table
    def create_new_entry():
        pass

    ## function to read from the table
    def get_all_items():
        pass
