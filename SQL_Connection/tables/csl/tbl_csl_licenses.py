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

from APICore.result_models.csl.licenses import CSLLicense, CSLLicenseBase
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal
from SQL_Connection.tables.csl.tbl_csl_licensePermissions import (
    create_new_license_permission,
)


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblCSLLicenses(Base):
    __tablename__ = "licenses"
    __table_args__ = {"schema": "csl"}

    id: Mapped[UUID] = mapped_column(
        Uuid(), primary_key=True, index=True, nullable=False
    )
    productId: Mapped[UUID] = mapped_column(
        ForeignKey("csl.products.id"), nullable=False
    )
    serialNumber: Mapped[str] = mapped_column(String(100), nullable=False)
    subscriptionStartDate: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    subscriptionEndDate: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    licenseType: Mapped[str] = mapped_column(String(15), nullable=False)
    licenseCount: Mapped[int] = mapped_column(Integer(), nullable=False)
    autorenew: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    autorenewLicenseCount: Mapped[int] = mapped_column(Integer(), nullable=False)
    createdAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    createdById: Mapped[UUID] = mapped_column(
        ForeignKey("accounts.users.id"), nullable=False
    )
    updatedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    updatedById: Mapped[UUID] = mapped_column(
        ForeignKey("accounts.users.id"), nullable=False
    )
    refreshedId: Mapped[UUID] = mapped_column(
        ForeignKey("core.refreshed.id"), nullable=False
    )


## function to write to create a new entry item in the table
def create_new_license(
    item: CSLLicense, refreshed, session: Session = None
) -> CSLLicense:
    base_item = CSLLicenseBase(**item.model_dump(exclude_defaults=True))
    new_entry = TblCSLLicenses(
        **base_item.model_dump(exclude_defaults=True), refreshedId=refreshed.id
    )
    if session is None:
        db = SessionLocal()
    try:
        new_entry = read_db_license(item, db)
    except NotFoundError:
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
        if item.permissions != []:
            [
                create_new_license_permission(permission, refreshed, db)
                for permission in item.permissions
            ]
    finally:
        db.close()
    return new_entry


## function to read from the table
def read_db_license(item: CSLLicense, db: Session) -> CSLLicense:
    result = db.query(TblCSLLicenses).filter(TblCSLLicenses.id == item.id).first()
    if result is None:
        raise NotFoundError(f"LicenseId: {item.id} not found")
    return result


## function to update the table
def update_db_license():
    pass


## function to delete from the table
def delete_db_license():
    pass
