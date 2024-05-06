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

from APICore.result_models.pal.doc_sessions import PALDocSession, PALDocSessionBase
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal
from SQL_Connection.tables.pal.tbl_pal_log_addins import create_new_log_addin
from SQL_Connection.tables.pal.tbl_pal_log_events import create_new_log_event
from SQL_Connection.tables.pal.tbl_pal_log_links import create_new_log_link
from SQL_Connection.tables.pal.tbl_pal_log_machines import create_new_log_machine
from SQL_Connection.tables.pal.tbl_pal_log_prints import create_new_log_print
from SQL_Connection.tables.pal.tbl_pal_log_summaries import create_new_log_summary
from SQL_Connection.tables.pal.tbl_pal_log_view_types import create_new_log_view_type
from SQL_Connection.tables.pal.tbl_pal_log_warning_summaries import (
    create_new_log_warning_summary,
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
def create_new_doc_session(
    item: PALDocSession,
    refreshed,
    session: Session = None,
) -> PALDocSession:
    base_content = PALDocSessionBase(**item.model_dump())
    base_content.refreshedId = refreshed.id
    new_entry = TblPALDocSessions(**base_content.model_dump(exclude_none=True))
    if session is None:
        db = SessionLocal()
        try:
            new_entry = read_db_doc_session(item, db)
        except NotFoundError:
            db.add(new_entry)
            db.commit()
            db.refresh(new_entry)
            if item.logAddIns != []:
                [create_new_log_addin(addin, refreshed, db) for addin in item.logAddIns]
            if item.logEvents != []:
                [create_new_log_event(event, refreshed, db) for event in item.logEvents]
            if item.logLinks != []:
                [create_new_log_link(link, refreshed, db) for link in item.logLinks]
            if item.logMachines != []:
                [
                    create_new_log_machine(machine, refreshed, db)
                    for machine in item.logMachines
                ]
            if item.logPrints != []:
                [
                    create_new_log_print(print_item, refreshed, db)
                    for print_item in item.logPrints
                ]
            if item.logSummaries != []:
                [
                    create_new_log_summary(summary, refreshed, db)
                    for summary in item.logSummaries
                ]
            if item.logViewTypes != []:
                [
                    create_new_log_view_type(view_type, refreshed, db)
                    for view_type in item.logViewTypes
                ]
            if item.logWarningSummaries != []:
                [
                    create_new_log_warning_summary(warning, refreshed, db)
                    for warning in item.logWarningSummaries
                ]
        finally:
            db.close()
    else:
        try:
            new_entry = read_db_doc_session(item, session)
        except NotFoundError:
            session.add(new_entry)
            session.commit()
            session.refresh(new_entry)
    return new_entry


## function to read the database for the item
def read_db_doc_session(item: PALDocSession, db: Session) -> PALDocSession:
    db_item = (
        db.query(TblPALDocSessions).filter(TblPALDocSessions.id == item.id).first()
    )
    if db_item is None:
        raise NotFoundError(f"DocSessionId: {item.id} not found")
    db_item_dump = {}
    for key, value in db_item.__dict__.items():
        db_item_dump.update({key: value})
    return PALDocSession(**db_item_dump)


## function to update the database for the item
def update_db_doc_session():
    pass


## function to delete the database for the item
def delete_db_doc_session():
    pass
