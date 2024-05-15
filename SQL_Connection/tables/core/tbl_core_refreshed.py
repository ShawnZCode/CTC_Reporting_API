from datetime import datetime, timedelta
from uuid import UUID, uuid4

from pydantic import BaseModel
from sqlalchemy import DateTime, Float, Integer, Uuid
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
    refreshStartedAt: Mapped[datetime] = mapped_column(
        DateTime(), default=datetime.now(), index=True, nullable=False
    )
    refreshFinishedAt: Mapped[datetime] = mapped_column(
        DateTime(), nullable=True, index=True
    )
    refreshDuarationMinutes: Mapped[float] = mapped_column(
        Float(2), nullable=True, index=True
    )


## function to write to create a new entry item in the table
def create_new_refreshed(session: Session = None) -> Refreshed:
    # pass
    new_entry = TblCoreRefreshed(id=uuid4(), refreshStartedAt=datetime.now())
    if session is None:
        db = SessionLocal()
        try:
            db.add(new_entry)
            db.commit()
            db.refresh(new_entry)
        finally:
            db.close()
    else:
        try:
            session.add(new_entry)
            session.commit()
            session.refresh(new_entry)
        except Exception as e:
            session.rollback()
            raise e
    return Refreshed(**new_entry.__dict__)


## function to read from the table
def get_last_refreshed(session: Session = None) -> Refreshed:
    try:
        db = SessionLocal()
        db_item = (
            db.query(TblCoreRefreshed)
            .order_by(TblCoreRefreshed.refreshStartedAt.desc())
            .first()
        )
        db.close()
    except NotFoundError:
        raise NotFoundError("No previous refresh records found")
    return Refreshed(**db_item.__dict__)


def get_refreshed_count(session: Session = None) -> int:
    if session is None:
        try:
            db = SessionLocal()
            count = db.query(TblCoreRefreshed).count()
        finally:
            db.close()
    else:
        count = session.query(TblCoreRefreshed).count()
    return count


## function to update last refreshed
def update_last_refreshed(refreshed: Refreshed, session: Session = None) -> Refreshed:
    db = SessionLocal()
    try:
        db_item = (
            db.query(TblCoreRefreshed)
            .filter(TblCoreRefreshed.id == refreshed.id)
            .first()
        )
        start_time = db_item.refreshStartedAt
        end_time = datetime.now()
        db_item.refreshFinishedAt = end_time
        db_item.refreshDuarationMinutes = (end_time - start_time).total_seconds() / 60
        db.commit()
        db.refresh(db_item)
    finally:
        db.close()
    return Refreshed(**db_item.__dict__)
