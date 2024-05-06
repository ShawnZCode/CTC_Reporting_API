from datetime import datetime
from uuid import UUID  # , uuid4

from pydantic import BaseModel
from sqlalchemy import (
    Boolean,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Table,
    Uuid,
)
from sqlalchemy.orm import Mapped, Session, mapped_column

from APICore.result_models.pal.doc_sessions import PALLogEvent
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblPALLogEvents(Base):
    __tablename__ = "logEvents"
    __table_args__ = {"schema": "pal"}

    id: Mapped[UUID] = mapped_column(
        Uuid(), primary_key=True, index=True, nullable=False
    )
    docSessionId: Mapped[UUID] = mapped_column(
        ForeignKey("pal.docSessions.id"), nullable=False
    )
    eventId: Mapped[int] = mapped_column(Integer(), nullable=False)
    eventType: Mapped[str] = mapped_column(String(10), nullable=True)
    eventName: Mapped[str] = mapped_column(String(25), nullable=True)
    viewName: Mapped[str] = mapped_column(String(255), nullable=True)
    viewId: Mapped[int] = mapped_column(Integer(), nullable=True)
    openViewCt: Mapped[int] = mapped_column(Integer(), nullable=False)
    eventDuration: Mapped[float] = mapped_column(Float(), nullable=False)
    actionCt: Mapped[int] = mapped_column(Integer(), nullable=False)
    activeWorksetName: Mapped[str] = mapped_column(String(255), nullable=True)
    familyWorksetOpenCt: Mapped[int] = mapped_column(Integer(), nullable=True)
    familyWorksetEditCt: Mapped[int] = mapped_column(Integer(), nullable=True)
    standardWorksetOpenCt: Mapped[int] = mapped_column(Integer(), nullable=True)
    standardWorksetEditCt: Mapped[int] = mapped_column(Integer(), nullable=True)
    userWorksetOpenCt: Mapped[int] = mapped_column(Integer(), nullable=True)
    userWorksetEditCt: Mapped[int] = mapped_column(Integer(), nullable=True)
    viewWorksetOpenCt: Mapped[int] = mapped_column(Integer(), nullable=True)
    viewWorksetEditCt: Mapped[int] = mapped_column(Integer(), nullable=True)
    logDate: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    addedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    uploadedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    refreshedId: Mapped[UUID] = mapped_column(
        ForeignKey("core.refreshed.id"), nullable=False
    )


## function to write to create a new entry item in the table
def create_new_log_event(
    item: PALLogEvent,
    refreshed,
    session: Session = None,
) -> PALLogEvent:
    base_item = PALLogEvent(**item.model_dump(exclude_none=True))
    new_entry = TblPALLogEvents(
        **base_item.model_dump(exclude_none=True), refreshedId=refreshed.id
    )
    if session is None:
        db = SessionLocal()
        try:
            new_entry = read_db_log_event(item, db)
        except NotFoundError:
            db.add(new_entry)
            db.commit()
            db.refresh(new_entry)
        finally:
            db.close()
    else:
        try:
            new_entry = read_db_log_event(item, session)
        except NotFoundError:
            session.add(new_entry)
            session.commit()
            session.refresh(new_entry)
    return new_entry


## function to read item from the table
def read_db_log_event(item: PALLogEvent, session: Session) -> PALLogEvent:
    db_item = (
        session.query(TblPALLogEvents).filter(TblPALLogEvents.id == item.id).first()
    )
    if db_item is None:
        raise NotFoundError(f"LogEventId: {item.id} not found")
    db_item_dump = {}
    for key, value in db_item.__dict__.items():
        db_item_dump.update({key: value})
    return PALLogEvent(**db_item_dump)


## function to update the table
def update_log_event():
    pass


## function to delete item from the table
def delete_log_event():
    pass
