from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel
from sqlalchemy import DateTime, Uuid
from sqlalchemy.orm import Mapped, Session, mapped_column

from APICore.result_models.core.refreshed import Refreshed
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal, get_db


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblCoreRefreshed(Base):
    __tablename__ = "refreshed"
    __table_args__ = {"schema": "core"}

    id: Mapped[uuid4] = mapped_column(
        Uuid(), default=uuid4(), primary_key=True, index=True, nullable=False
    )
    refreshedAt: Mapped[datetime] = mapped_column(
        DateTime(), default=datetime.now(), index=True, nullable=False
    )


## function to write to create a new entry item in the table
def create_new_refreshed(session: Session = Session(get_db)) -> Refreshed:
    # pass
    new_entry = TblCoreRefreshed(id=uuid4(), refreshedAt=datetime.now())
    db = SessionLocal()
    try:
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
    finally:
        db.close()
    return new_entry


## function to read from the table
def get_last_refreshed(session: Session) -> Refreshed:
    try:
        db = SessionLocal()
        item = (
            db.query(TblCoreRefreshed)
            .order_by(TblCoreRefreshed.refreshedAt.desc())
            .first()
        )
        db.close()
    except NotFoundError:
        raise NotFoundError("No previous refresh records found")
    return item
