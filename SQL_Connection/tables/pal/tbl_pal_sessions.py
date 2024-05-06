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

from APICore.result_models.pal.sessions import PALSession
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblPALSessions(Base):
    __tablename__ = "sessions"
    __table_args__ = {"schema": "pal"}

    id: Mapped[UUID] = mapped_column(
        Uuid(), primary_key=True, index=True, nullable=False
    )
    sessionId: Mapped[UUID] = mapped_column(Uuid(), nullable=False)
    revitVersion: Mapped[str | int] = mapped_column(String(20), nullable=True)
    userName: Mapped[str] = mapped_column(String(50), nullable=False)
    machineName: Mapped[str] = mapped_column(String(50), nullable=False)
    isOpen: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    logDate: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    uploadedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    addedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    refreshedId: Mapped[UUID] = mapped_column(
        ForeignKey("core.refreshed.id"), nullable=False
    )


## function to write new entry item to the table
def create_new_session(
    item: PALSession, refreshed, session: Session = None
) -> PALSession:
    base_content = PALSession(**item.model_dump())
    base_content.refreshedId = refreshed.id
    new_entry = TblPALSessions(**base_content.model_dump(exclude_none=True))
    if session is None:
        db = SessionLocal()
        try:
            new_entry = read_db_session(item, db)
        except NotFoundError:
            db.add(new_entry)
            db.commit()
            db.refresh(new_entry)
        finally:
            db.close()
    else:
        try:
            new_entry = read_db_session(item, session)
        except NotFoundError:
            session.add(new_entry)
            session.commit()
            session.refresh(new_entry)
    return new_entry


## function to read the database for the item
def read_db_session(item: PALSession, db: Session) -> PALSession:
    db_item = db.query(TblPALSessions).filter(TblPALSessions.id == item.id).first()
    if db_item is None:
        raise NotFoundError(f"SessionId: {item.id} not found")
    db_item_dump = {}
    for key, value in db_item.__dict__.items():
        db_item_dump.update({key: value})
    return PALSession(**db_item_dump)


## function to update the database for the item
def update_db_session():
    pass


## function to delete the database for the item
def delete_db_session():
    pass
