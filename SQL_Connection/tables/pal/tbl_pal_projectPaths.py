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

from APICore.result_models.pal.projects import PALProjectPath
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblPALProjectPaths(Base):
    __tablename__ = "projectPaths"
    __table_args__ = {"schema": "pal"}

    id: Mapped[UUID] = mapped_column(
        Uuid(), primary_key=True, index=True, nullable=False
    )
    centralFilePath: Mapped[str] = mapped_column(String(2048), nullable=False)
    addedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    addedById: Mapped[UUID] = mapped_column(
        ForeignKey("accounts.users.id"), nullable=False
    )
    updatedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    updatedById: Mapped[UUID] = mapped_column(
        ForeignKey("accounts.users.id"), nullable=False
    )
    projectId: Mapped[UUID] = mapped_column(
        ForeignKey("pal.projects.id"), nullable=True, default=None
    )
    refreshedId: Mapped[UUID] = mapped_column(
        ForeignKey("core.refreshed.id"), nullable=False
    )


## function to write a new project entry item in the table
def create_new_project_path(
    item: PALProjectPath,
    refreshed,
    session: Session = None,
) -> PALProjectPath:
    base_path = PALProjectPath(**item.model_dump())
    new_entry = TblPALProjectPaths(
        **base_path.model_dump(exclude_none=True),
        refreshedId=refreshed.id,
    )
    if session is None:
        db = SessionLocal()
        try:
            new_entry = read_db_project_path(item, db)
        except NotFoundError:
            db.add(new_entry)
            db.commit()
            db.refresh(new_entry)
        finally:
            db.close()
    else:
        try:
            new_entry = read_db_project_path(item, session)
        except NotFoundError:
            session.add(new_entry)
            session.commit()
            session.refresh(new_entry)
    return new_entry


## function to read a project entry item in the table
def read_db_project_path(item: PALProjectPath, db: Session) -> PALProjectPath | None:
    db_project_path = db.query(TblPALProjectPaths).filter_by(id=item.id).first()
    if db_project_path is None:
        raise NotFoundError(f"PathId {item.id} not found in database")
    else:
        return db_project_path
