from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Uuid,
)
from sqlalchemy.orm import Mapped, Session, mapped_column

from APICore.result_models.csl.licenses import CSLLicensePermission
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblCSLLicensePermissions(Base):
    __tablename__ = "licensePermissions"
    __table_args__ = {"schema": "csl"}

    id: Mapped[UUID] = mapped_column(
        Uuid(), primary_key=True, index=True, nullable=False
    )
    resourceId: Mapped[UUID] = mapped_column(Uuid(), nullable=False)
    resourceType: Mapped[str] = mapped_column(String(15), nullable=False)
    addedById: Mapped[UUID] = mapped_column(
        ForeignKey("accounts.users.id"), nullable=False
    )
    addedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    refreshedId: Mapped[UUID] = mapped_column(
        ForeignKey("core.refreshed.id"), nullable=False
    )


## function to write to create a new entry item in the table
def write_db_license_permission(
    item: CSLLicensePermission, refreshed, session: Session = None
) -> CSLLicensePermission:
    new_entry = TblCSLLicensePermissions(
        **item.model_dump(exclude_defaults=True), refreshedId=refreshed.id
    )
    if session is None:
        db = SessionLocal()
        try:
            new_entry = read_db_license_permission(item, db)
        except NotFoundError:
            db.add(new_entry)
            db.commit()
            db.refresh(new_entry)
        finally:
            db.close()
    else:
        try:
            new_entry = read_db_license_permission(item, session)
        except NotFoundError:
            session.add(new_entry)
            session.commit()
            session.refresh(new_entry)
    return new_entry


def read_db_license_permission(
    item: CSLLicensePermission, db: Session
) -> CSLLicensePermission:
    """Read the database for the item"""
    db_item = db.query(TblCSLLicensePermissions).filter_by(id=item.id).first()
    if db_item is None:
        raise NotFoundError(f"LicensePermissionId: {item.id} not found")
    db_item_dump = {}
    for key, value in db_item.__dict__.items():
        db_item_dump.update({key: value})
    return CSLLicensePermission(**db_item_dump)
