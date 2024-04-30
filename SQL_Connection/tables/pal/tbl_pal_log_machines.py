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

from APICore.result_models.pal.doc_sessions import PALLogMachine
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblPALLogMachines(Base):
    __tablename__ = "logMachines"
    __table_args__ = {"schema": "pal"}

    id: Mapped[UUID] = mapped_column(
        Uuid(), primary_key=True, index=True, nullable=False
    )
    docSessionId: Mapped[UUID] = mapped_column(
        Uuid(), ForeignKey("pal.docSessions.id"), nullable=False
    )
    machineName: Mapped[str] = mapped_column(String(255), nullable=False)
    processorId: Mapped[str] = mapped_column(String(255), nullable=False)
    mac: Mapped[str] = mapped_column(String(20), nullable=False)
    operatingSystem: Mapped[str] = mapped_column(String(255), nullable=False)
    hdd: Mapped[str] = mapped_column(String(255), nullable=False)
    motherboard: Mapped[str] = mapped_column(String(255), nullable=False)
    bios: Mapped[str] = mapped_column(String(255), nullable=False)
    ram: Mapped[int] = mapped_column(Integer(), nullable=False)
    slots: Mapped[int] = mapped_column(Integer(), nullable=False)
    cpu: Mapped[str] = mapped_column(String(255), nullable=False)
    video: Mapped[str] = mapped_column(String(255), nullable=False)
    ipaddress: Mapped[str] = mapped_column(String(20), nullable=False)
    logDate: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    addedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    uploadedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    refreshedId: Mapped[UUID] = mapped_column(
        ForeignKey("core.refreshed.id"), nullable=False
    )


## function to write to create a new entry item in the table
def create_new_log_machine(
    item: PALLogMachine,
    refreshed,
    session: Session = None,
) -> PALLogMachine:
    base_item = PALLogMachine(**item.model_dump(exclude_none=True))
    new_entry = TblPALLogMachines(
        **base_item.model_dump(exclude_none=True), refreshedId=refreshed.id
    )
    if session is None:
        db = SessionLocal()
        try:
            new_entry = read_db_log_machine(item, db)
        except NotFoundError:
            db.add(new_entry)
            db.commit()
            db.refresh(new_entry)
        finally:
            db.close()
    else:
        try:
            new_entry = read_db_log_machine(item, session)
        except NotFoundError:
            session.add(new_entry)
            session.commit()
            session.refresh(new_entry)
    return new_entry


## function to read item from the table
def read_db_log_machine(item: PALLogMachine, session: Session) -> PALLogMachine:
    db_item = (
        session.query(TblPALLogMachines).filter(TblPALLogMachines.id == item.id).first()
    )
    if db_item is None:
        raise NotFoundError(f"logMaghineId: {item.id} not found")
    return db_item
