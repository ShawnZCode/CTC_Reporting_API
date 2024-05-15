from datetime import datetime
from uuid import UUID  # , uuid4

from pydantic import BaseModel, ValidationError
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

from APICore.result_models.pal.doc_sessions import PALDocSession, PALDocSessionBase
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal
from SQL_Connection.tables.pal.tbl_pal_log_addins import write_db_log_addin
from SQL_Connection.tables.pal.tbl_pal_log_events import write_db_log_event
from SQL_Connection.tables.pal.tbl_pal_log_links import write_db_log_link
from SQL_Connection.tables.pal.tbl_pal_log_machines import write_db_log_machine
from SQL_Connection.tables.pal.tbl_pal_log_prints import write_db_log_print
from SQL_Connection.tables.pal.tbl_pal_log_summaries import write_db_log_summary
from SQL_Connection.tables.pal.tbl_pal_log_view_types import write_db_log_view_type
from SQL_Connection.tables.pal.tbl_pal_log_warning_summaries import (
    write_db_log_warning_summary,
)


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblPALDocSessions(Base):
    __tablename__ = "docSessions"
    __table_args__ = {"schema": "pal"}

    id: Mapped[UUID] = mapped_column(
        Uuid(), primary_key=True, index=True, nullable=False
    )
    projectId: Mapped[UUID] = mapped_column(Uuid(), nullable=True)
    userName: Mapped[str] = mapped_column(String(50), nullable=False)
    machineName: Mapped[str] = mapped_column(String(50), nullable=False)
    server: Mapped[str] = mapped_column(String(250), nullable=True)
    centralFileName: Mapped[str] = mapped_column(String(255), nullable=False)
    centralFilePath: Mapped[str] = mapped_column(String(255), nullable=False)
    shortFileName: Mapped[str] = mapped_column(String(100), nullable=False)
    localFileName: Mapped[str] = mapped_column(String(255), nullable=False)
    localFileSize: Mapped[int] = mapped_column(Integer(), nullable=False)
    revitVersion: Mapped[str] = mapped_column(String(50), nullable=False)
    isAudit: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    openingDuration: Mapped[float] = mapped_column(Float(), nullable=False)
    worksetCt: Mapped[int] = mapped_column(Integer(), nullable=False)
    worksetEditCt: Mapped[int] = mapped_column(Integer(), nullable=False)
    worksetOpenCt: Mapped[int] = mapped_column(Integer(), nullable=False)
    basePoint: Mapped[str] = mapped_column(String(50), nullable=False)
    surveyPoint: Mapped[str] = mapped_column(String(50), nullable=False)
    angleToTrueNorth: Mapped[float] = mapped_column(Float(), nullable=False)
    siteLatLong: Mapped[str] = mapped_column(String(50), nullable=False)
    status: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    logDate: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    uploadedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    addedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    refreshedId: Mapped[UUID] = mapped_column(
        ForeignKey("core.refreshed.id"), nullable=False
    )


## function to write new entry item to the table
def write_db_doc_session(
    item: PALDocSession,
    refreshed,
    session: Session = None,
) -> PALDocSession:
    base_content = PALDocSessionBase(**item.model_dump())
    base_content.refreshedId = refreshed.id
    db_item_orig = TblPALDocSessions(**base_content.model_dump(exclude_none=True))
    db_item = db_item_orig
    if session is None:
        db = SessionLocal()
    else:
        db = session
    try:
        read_db_doc_session(item, db)
    except NotFoundError:
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        if item.logAddIns != []:
            [write_db_log_addin(addin, refreshed, db) for addin in item.logAddIns]
        if item.logEvents != []:
            [write_db_log_event(event, refreshed, db) for event in item.logEvents]
        if item.logLinks != []:
            [write_db_log_link(link, refreshed, db) for link in item.logLinks]
        if item.logMachines != []:
            [
                write_db_log_machine(machine, refreshed, db)
                for machine in item.logMachines
            ]
        if item.logPrints != []:
            [
                write_db_log_print(print_item, refreshed, db)
                for print_item in item.logPrints
            ]
        if item.logSummaries != []:
            [
                write_db_log_summary(summary, refreshed, db)
                for summary in item.logSummaries
            ]
        if item.logViewTypes != []:
            [
                write_db_log_view_type(view_type, refreshed, db)
                for view_type in item.logViewTypes
            ]
        if item.logWarningSummaries != []:
            [
                write_db_log_warning_summary(warning, refreshed, db)
                for warning in item.logWarningSummaries
            ]
    if session is None:
        db.close()
    try:
        return PALDocSession(**db_item.__dict__)
    except ValidationError:
        return item


## function to read the database for the item
def read_db_doc_session(item: PALDocSession, db: Session) -> PALDocSession:
    db_item = (
        db.query(TblPALDocSessions).filter(TblPALDocSessions.id == item.id).first()
    )
    if db_item is None:
        raise NotFoundError(f"DocSessionId: {item.id} not found")
    return PALDocSession(**db_item.__dict__)


## function to update the database for the item
def update_db_doc_session():
    pass


## function to delete the database for the item
def delete_db_doc_session():
    pass
