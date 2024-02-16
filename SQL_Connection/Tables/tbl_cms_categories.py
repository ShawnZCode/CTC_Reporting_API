from sqlalchemy import String, Integer, ForeignKey
from uuid import UUID, uuid4
from sqlalchemy.orm import mapped_column, Mapped
from SQL_Connection.db_connection import Base
from pydantic import BaseModel


## creating the pydantic BaseModel
class CMS_Categories(BaseModel):
    id: int
    name: str
    fileExtension: str
    type: str
    refreshedId: UUID

## Using SQLAlchemy2.0 generate Table with association to the correct schema
class Tbl_CMS_Categories(Base):
    __tablename__ = 'categories'
    __table_args__ = {"schema": "cms"}

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    fileExtension: Mapped[str] = mapped_column(String(20), nullable=False)
    type: Mapped[str] = mapped_column(String(100), nullable=False)
    refreshedId: Mapped[uuid4] = mapped_column(ForeignKey('core.refreshed.id'), nullable=False)

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
