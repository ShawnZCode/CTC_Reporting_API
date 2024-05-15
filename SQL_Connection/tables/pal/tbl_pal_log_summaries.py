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

from APICore.result_models.pal.doc_sessions import PALLogSummary
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblPALLogSummaries(Base):
    __tablename__ = "logSummaries"
    __table_args__ = {"schema": "pal"}

    id: Mapped[UUID] = mapped_column(
        Uuid(), primary_key=True, index=True, nullable=False
    )
    docSessionId: Mapped[UUID] = mapped_column(
        Uuid(), ForeignKey("pal.docSessions.id"), nullable=False
    )
    eventId: Mapped[int] = mapped_column(Integer, nullable=False)
    groupCt: Mapped[int] = mapped_column(Integer, nullable=False)
    inPlaceCt: Mapped[int] = mapped_column(Integer, nullable=False)
    unPlacedRoomCt: Mapped[int] = mapped_column(Integer, nullable=False)
    unenclosedRoomCt: Mapped[int] = mapped_column(Integer, nullable=False)
    placedRoomCt: Mapped[int] = mapped_column(Integer, nullable=False)
    unPlacedSpaceCt: Mapped[int] = mapped_column(Integer, nullable=False)
    unenclosedSpaceCt: Mapped[int] = mapped_column(Integer, nullable=False)
    placedSpaceCt: Mapped[int] = mapped_column(Integer, nullable=False)
    viewCt: Mapped[int] = mapped_column(Integer, nullable=False)
    phaseCt: Mapped[int] = mapped_column(Integer, nullable=False)
    desOptCt: Mapped[int] = mapped_column(Integer, nullable=False)
    worksetCt: Mapped[int] = mapped_column(Integer, nullable=False)
    familyCt: Mapped[int] = mapped_column(Integer, nullable=False)
    instanceCt: Mapped[int] = mapped_column(Integer, nullable=False)
    materialCt: Mapped[int] = mapped_column(Integer, nullable=False)
    viewFilterCt: Mapped[int] = mapped_column(Integer, nullable=False)
    unplacedFamilyCt: Mapped[int] = mapped_column(Integer, nullable=False)
    levelCt: Mapped[int] = mapped_column(Integer, nullable=False)
    warningCt: Mapped[int] = mapped_column(Integer, nullable=False)
    warningTypeCt: Mapped[int] = mapped_column(Integer, nullable=False)
    logDate: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    addedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    uploadedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    refreshedId: Mapped[UUID] = mapped_column(
        ForeignKey("core.refreshed.id"), nullable=False
    )


## function to write new entry item to the table
def write_db_log_summary(
    item: PALLogSummary,
    refreshed,
    session: Session = None,
) -> PALLogSummary:
    base_item = item.model_dump(exclude_none=True)
    db_item = TblPALLogSummaries(**base_item, refreshedId=refreshed.id)
    if session is None:
        db = SessionLocal()
    else:
        db = session
    try:
        read_db_log_summary(item, db)
    except NotFoundError:
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
    if session is None:
        db.close()
    return PALLogSummary(**db_item.__dict__)


## function to read item from the table
def read_db_log_summary(item: PALLogSummary, session: Session) -> PALLogSummary:
    db_item = (
        session.query(TblPALLogSummaries)
        .filter(TblPALLogSummaries.id == item.id)
        .first()
    )
    if db_item is None:
        raise NotFoundError(f"LogSummaryId: {item.id} not found")
    return PALLogSummary(**db_item.__dict__)


## function to update the table
def update_log_summary():
    pass


## function to delete item from the table
def delete_log_summary():
    pass
