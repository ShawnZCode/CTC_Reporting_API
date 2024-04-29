from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from sqlalchemy import (
    Boolean,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Uuid,
)
from sqlalchemy.orm import Mapped, Session, mapped_column

from APICore.result_models.csl.app_sessions import CSLAppSession
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblCSLAppSessions(Base):
    __tablename__ = "app_sessions"
    __table_args__ = {"schema": "csl"}

    id: Mapped[uuid4] = mapped_column(
        Uuid(), primary_key=True, index=True, nullable=False
    )
    productId: Mapped[uuid4] = mapped_column(
        ForeignKey("csl.products.id"), nullable=False
    )
    productName: Mapped[str] = mapped_column(String(100), nullable=True)
    productVersion: Mapped[str] = mapped_column(String(15), nullable=True)
    startedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=True)
    endedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=True)
    computerName: Mapped[str] = mapped_column(String(100), nullable=True)
    userId: Mapped[uuid4] = mapped_column(
        Uuid(), nullable=True
    )  # ForeignKey("accounts.users.id"),
    applicationName: Mapped[str] = mapped_column(String(100), nullable=True)
    autodeskVersionNumber: Mapped[str] = mapped_column(String(15), nullable=True)
    autodeskSubVersionNumber: Mapped[str] = mapped_column(String(15), nullable=True)
    autodeskBuildNumber: Mapped[str] = mapped_column(String(25), nullable=True)
    refreshedId: Mapped[uuid4] = mapped_column(
        ForeignKey("core.refreshed.id"), nullable=False
    )


## function to write to create a new entry item in the table
def create_new_app_session(
    item: CSLAppSession, refreshed, session: Session = None
) -> CSLAppSession:
    base_item = item.model_dump(exclude_defaults=True)
    new_entry = TblCSLAppSessions(**base_item, refreshedId=refreshed.id)
    if session is None:
        db = SessionLocal()
    else:
        db = session
    try:
        new_entry = read_db_app_session(item, db)
    except NotFoundError:
        # if new_entry.id is not None:  # = "00000000-0000-0000-0000-000000000000":
        try:
            db.add(new_entry)
            db.commit()
            db.refresh(new_entry)
        except Exception as e:
            pass
    return new_entry


## function to read from the database
def read_db_app_session(item: CSLAppSession, db: Session) -> CSLAppSession:
    result = db.query(TblCSLAppSessions).filter(TblCSLAppSessions.id == item.id).first()
    if result is None:
        raise NotFoundError(f"AppSessionID: {item.id} not found")
    return result


## function to update an entry in the database
def update_db_app_session():
    pass


## function to delete an entry in the database
def delete_db_app_session():
    pass
