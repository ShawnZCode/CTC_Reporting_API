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

from APICore.result_models.pal.projects import PALProject, PALProjectBase
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal
from SQL_Connection.tables.pal.tbl_pal_projectPaths import create_new_project_path


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblPALProjects(Base):
    __tablename__ = "projects"
    __table_args__ = {"schema": "pal"}

    id: Mapped[UUID] = mapped_column(
        Uuid(), primary_key=True, index=True, nullable=False
    )
    projectNumber: Mapped[str] = mapped_column(String(50), nullable=False)
    projectName: Mapped[str] = mapped_column(String(150), nullable=True)
    status: Mapped[str] = mapped_column(String(30), nullable=False)
    office: Mapped[str] = mapped_column(String(30), nullable=True)
    buildingName: Mapped[str] = mapped_column(String(50), nullable=True)
    clientName: Mapped[str] = mapped_column(String(50), nullable=True)
    streetAddress: Mapped[str] = mapped_column(String(50), nullable=True)
    streetAddress2: Mapped[str] = mapped_column(String(50), nullable=True)
    streetAddress3: Mapped[str] = mapped_column(String(50), nullable=True)
    projectPhase: Mapped[str] = mapped_column(String(30), nullable=True)
    projectIssueDate: Mapped[datetime] = mapped_column(DateTime(), nullable=True)
    projectOwner: Mapped[str] = mapped_column(String(50), nullable=True)
    city: Mapped[str] = mapped_column(String(30), nullable=True)
    stateorProvince: Mapped[str] = mapped_column(String(30), nullable=True)
    postalCode: Mapped[str] = mapped_column(String(15), nullable=True)
    county: Mapped[str] = mapped_column(String(30), nullable=True)
    contact: Mapped[str] = mapped_column(String(50), nullable=True)
    addedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    addedById: Mapped[UUID] = mapped_column(
        ForeignKey("accounts.users.id"), nullable=False
    )
    updatedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    updatedById: Mapped[UUID] = mapped_column(
        ForeignKey("accounts.users.id"), nullable=False
    )
    refreshedId: Mapped[UUID] = mapped_column(
        ForeignKey("core.refreshed.id"), nullable=False
    )


## function to write a new project entry item in the table
def create_new_project(
    item: PALProject,
    refreshed,
    session: Session = None,
) -> PALProject:
    base_project = PALProjectBase(**item.model_dump())
    base_project.refreshedId = refreshed.id
    new_entry = TblPALProjects(**base_project.model_dump(exclude_none=True))
    if session is None:
        db = SessionLocal()
        try:
            new_entry = read_db_project(item, db)
        except NotFoundError:
            try:
                db.add(new_entry)
                db.commit()
                db.refresh(new_entry)
                if item.projectPaths != []:
                    [
                        create_new_project_path(path, refreshed)
                        for path in item.projectPaths
                    ]
            except Exception as e:
                return e
        finally:
            db.close()
    else:
        try:
            new_entry = read_db_project(item, session)
        except NotFoundError:
            try:
                session.add(new_entry)
                session.commit()
                session.refresh(new_entry)
            except Exception as e:
                return e

    return new_entry


## function to read a project entry item in the table
def read_db_project(item: PALProject, session: Session) -> PALProject:
    db_item = session.query(TblPALProjects).filter(TblPALProjects.id == item.id).first()
    if db_item is None:
        raise NotFoundError(f"projectId: {item.id} not found in the database")
    else:
        return db_item


## function to update a project entry item in the table
def update_db_project():
    pass


## function to delete a project entry item in the table
def delete_db_project():
    pass
