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

from APICore.result_models.pal.doc_sessions import PALLogWarningSummary
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblPALLogWarningSummaries(Base):
    __tablename__ = "logWarningSummaries"
    __table_args__ = {"schema": "pal"}

    id: Mapped[UUID] = mapped_column(
        Uuid(), primary_key=True, index=True, nullable=False
    )
    docSessionId: Mapped[UUID] = mapped_column(
        Uuid(), ForeignKey("pal.docSessions.id"), nullable=False
    )
    warningCt: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    elementIds: Mapped[str] = mapped_column(String(2000), nullable=False)
    logDate: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    addedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    uploadedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    refreshedId: Mapped[UUID] = mapped_column(
        ForeignKey("core.refreshed.id"), nullable=False
    )


## function to write new entry item to the table
def write_db_log_warning_summary(
    item: PALLogWarningSummary,
    refreshed,
    session: Session = None,
) -> PALLogWarningSummary:
    base_item = item.model_dump(exclude_none=True)
    db_item = TblPALLogWarningSummaries(**base_item, refreshedId=refreshed.id)
    if session is None:
        db = SessionLocal()
    else:
        db = session
    try:
        read_db_log_warning_summary(item, db)
    except NotFoundError:
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
    finally:
        db.close()
    return PALLogWarningSummary(**db_item.__dict__)


## function to read item from the table
def read_db_log_warning_summary(
    item: PALLogWarningSummary,
    session: Session,
) -> PALLogWarningSummary:
    db_item = (
        session.query(TblPALLogWarningSummaries)
        .filter(TblPALLogWarningSummaries.id == item.id)
        .first()
    )
    if db_item is None:
        raise NotFoundError(f"LogWarningSummaryId: {item.id} not found")
    return PALLogWarningSummary(**db_item.__dict__)


## function to update the database for the item
def update_log_warning_summary():
    pass


## function to delete the database for the item
def delete_log_warning_summary():
    pass
