from uuid import UUID, uuid4

from pydantic import BaseModel
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from APICore.result_models.cms.content_categories import CMSCategory
from SQL_Connection.db_connection import Base


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblCMSCategories(Base):
    __tablename__ = "categories"
    __table_args__ = {"schema": "cms"}

    id: Mapped[int] = mapped_column(
        Integer(), primary_key=True, index=True, nullable=False
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    fileExtension: Mapped[str] = mapped_column(String(20), nullable=False)
    type: Mapped[str] = mapped_column(String(100), nullable=False)
    refreshedId: Mapped[uuid4] = mapped_column(
        ForeignKey("core.refreshed.id"), nullable=False
    )


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
