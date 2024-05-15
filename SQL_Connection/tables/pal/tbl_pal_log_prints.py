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

from APICore.result_models.pal.doc_sessions import PALLogPrint
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblPALLogPrints(Base):
    __tablename__ = "logPrints"
    __table_args__ = {"schema": "pal"}

    id: Mapped[UUID] = mapped_column(
        Uuid(), primary_key=True, index=True, nullable=False
    )
    docSessionId: Mapped[UUID] = mapped_column(
        Uuid(), ForeignKey("pal.docSessions.id"), nullable=False
    )
    jobId: Mapped[int] = mapped_column(Integer, nullable=False)
    userName: Mapped[str] = mapped_column(String(100), nullable=False)
    printed: Mapped[str] = mapped_column(String(4000), nullable=False)
    failed: Mapped[str] = mapped_column(String(4000), nullable=False)
    printCt: Mapped[int] = mapped_column(Integer, nullable=False)
    failCt: Mapped[int] = mapped_column(Integer, nullable=False)
    jobStart: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    jobEnd: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    logDate: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    addedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    uploadedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    refreshedId: Mapped[UUID] = mapped_column(
        ForeignKey("core.refreshed.id"), nullable=False
    )


## function to write new entry item to the table
def write_db_log_print(
    item: PALLogPrint,
    refreshed,
    session: Session = None,
) -> PALLogPrint:
    base_item = item.model_dump(exclude_none=True)
    db_item = TblPALLogPrints(**base_item, refreshedId=refreshed.id)
    if session is None:
        db = SessionLocal()
    else:
        db = session
    try:
        read_db_log_print(item, db)
    except NotFoundError:
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
    if session is None:
        db.close()
    return PALLogPrint(**db_item.__dict__)


## function to read item from the table
def read_db_log_print(item: PALLogPrint, session: Session) -> PALLogPrint:
    db_item = (
        session.query(TblPALLogPrints).filter(TblPALLogPrints.id == item.id).first()
    )
    if db_item is None:
        raise NotFoundError(f"LogPrintId: {item.id} not found")
    return PALLogPrint(**db_item.__dict__)
