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
from SQL_Connection.tables.pal.tbl_pal_projectPaths import write_db_project_path
from SQL_Connection.tables.pal.tbl_pal_projectPermissions import (
    write_db_project_permission,
)


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
def write_db_project(
    item: PALProject,
    refreshed,
    session: Session = None,
) -> PALProject:
    base_project = PALProjectBase(**item.model_dump())
    base_project.refreshedId = refreshed.id
    db_item = TblPALProjects(**base_project.model_dump(exclude_none=True))
    if session is None:
        db = SessionLocal()
    else:
        db = session
    try:
        read_db_project(item, db)
    except NotFoundError:
        try:
            db.add(db_item)
            db.commit()
            db.refresh(db_item)
            if item.projectPaths != []:
                [
                    write_db_project_path(path, refreshed, db)
                    for path in item.projectPaths
                ]
            if item.projectPermissions != []:
                [
                    write_db_project_permission(permission, refreshed, db)
                    for permission in item.projectPermissions
                ]
        except Exception as e:
            return e
    if session is None:
        db.close()
    return PALProject(**db_item.__dict__)


## function to read a project entry item in the table
def read_db_project(item: PALProject, session: Session) -> PALProject:
    db_item = session.query(TblPALProjects).filter(TblPALProjects.id == item.id).first()
    if db_item is None:
        raise NotFoundError(f"projectId: {item.id} not found")
    db_item_dump = {}
    for key, value in db_item.__dict__.items():
        db_item_dump.update({key: value})
    return PALProject(**db_item_dump)


## function to update a project entry item in the table
def update_db_project():
    pass


## function to delete a project entry item in the table
def delete_db_project():
    pass
