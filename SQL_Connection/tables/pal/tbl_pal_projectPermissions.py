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

from APICore.result_models.pal.projects import PALProjectPermission
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblPALProjectPermissions(Base):
    __tablename__ = "projectPermissions"
    __table_args__ = {"schema": "pal"}

    id: Mapped[UUID] = mapped_column(
        Uuid(),
        primary_key=True,
        index=True,
        nullable=False,
    )
    projectId: Mapped[UUID] = mapped_column(
        Uuid(),
        ForeignKey("pal.projects.id"),
        nullable=False,
    )
    resourceId: Mapped[UUID] = mapped_column(
        Uuid(),
        nullable=False,
    )
    resourceType: Mapped[str] = mapped_column(String(50), nullable=False)
    projectRole: Mapped[str] = mapped_column(String(50), nullable=False)
    addedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    addedById: Mapped[UUID] = mapped_column(
        Uuid(),
        ForeignKey("accounts.users.id"),
        nullable=False,
    )
    updatedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    updatedById: Mapped[UUID] = mapped_column(
        Uuid(),
        ForeignKey("accounts.users.id"),
        nullable=False,
    )
    refreshedId: Mapped[UUID] = mapped_column(
        Uuid(),
        ForeignKey("core.refreshed.id"),
        nullable=False,
    )


## function to write a new project permission entry item in the table
def write_db_project_permission(
    item: PALProjectPermission,
    refreshed,
    session: Session = None,
) -> PALProjectPermission:
    db_item = TblPALProjectPermissions(
        **item.model_dump(exclude_none=True),
        refreshedId=refreshed.id,
    )
    if session is None:
        db = SessionLocal()
    else:
        db = session
    try:
        read_db_project_permission(item, db)
    except NotFoundError:
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
    finally:
        db.close()
    return PALProjectPermission(**db_item.__dict__)


## function to read a project permission entry item in the table
def read_db_project_permission(
    item: PALProjectPermission,
    session: Session,
) -> PALProjectPermission:
    db_item = (
        session.query(TblPALProjectPermissions)
        .filter(TblPALProjectPermissions.id == item.id)
        .first()
    )
    if db_item is None:
        raise NotFoundError(f"projectPermissionId: {item.id} not found")
    db_item_dump = {}
    for key, value in db_item.__dict__.items():
        db_item_dump.update({key: value})
    return PALProjectPermission(**db_item_dump)
