from uuid import UUID, uuid4

from pydantic import BaseModel
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, Session, mapped_column

from APICore.result_models.cms.content_categories import CMSCategory
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblCMSCategories(Base):
    __tablename__ = "categories"
    __table_args__ = {"schema": "cms"}

    id: Mapped[int] = mapped_column(
        Integer(), primary_key=True, index=True, nullable=False
    )
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    fileExtension: Mapped[str] = mapped_column(String(20), nullable=True)
    type: Mapped[str] = mapped_column(String(100), nullable=True)
    refreshedId: Mapped[uuid4] = mapped_column(
        ForeignKey("core.refreshed.id"), nullable=True
    )


## initialize the table
def __init__(self, id: int, displayName: str):
    self.id = id
    self.displayName = displayName


## function to write to create a new entry item in the table
def create_new_category(
    item: CMSCategory, refreshed, session: Session = None
) -> CMSCategory:
    base_category = CMSCategory(**item.model_dump())
    base_category.refreshedId = refreshed.id
    new_entry = TblCMSCategories(**base_category.model_dump(exclude_none=True))
    if session is None:
        db = SessionLocal()
        try:
            new_entry = read_db_category(item, db)
        except NotFoundError:
            db.add(new_entry)
            db.commit()
            db.refresh(new_entry)
        finally:
            db.close()
    else:
        db = session
        try:
            new_entry = read_db_category(item, db)
        except NotFoundError:
            db.add(new_entry)
            db.commit()
            db.refresh(new_entry)
    return new_entry


## function to read from the table
def read_db_category(item: CMSCategory, session: Session) -> CMSCategory:
    db_item = (
        session.query(TblCMSCategories).filter(TblCMSCategories.id == item.id).first()
    )
    if db_item is None:
        raise NotFoundError(f"CategoryId: {item.id} not found")
    db_item_dump = {}
    for key, value in db_item.__dict__.items():
        db_item_dump.update({key: value})
    return CMSCategory(**db_item_dump)
