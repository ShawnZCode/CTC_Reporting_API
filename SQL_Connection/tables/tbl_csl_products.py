from datetime import datetime
from uuid import UUID  # , uuid4

from pydantic import BaseModel
from sqlalchemy import (
    ForeignKey,
    String,
    Uuid,
)
from sqlalchemy.orm import Mapped, Session, mapped_column

from APICore.result_models.csl.products import CSLProduct, CSLProductBase
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal
from SQL_Connection.tables.tbl_csl_app_sessions import create_new_app_session


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblCSLProducts(Base):
    __tablename__ = "products"
    __table_args__ = {"schema": "csl"}

    id: Mapped[UUID] = mapped_column(
        Uuid(), primary_key=True, index=True, nullable=False
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    refreshedId: Mapped[UUID] = mapped_column(
        ForeignKey("core.refreshed.id"), nullable=False
    )


## function to write to create a new entry item in the table
def create_new_product(
    item: CSLProduct, refreshed, session: Session = None
) -> CSLProduct:
    base_item = CSLProductBase(**item.model_dump(exclude_defaults=True))
    new_entry = TblCSLProducts(
        **base_item.model_dump(exclude_defaults=True), refreshedId=refreshed.id
    )
    if session is None:
        db = SessionLocal()
    else:
        db = session
    try:
        new_entry = read_db_product(item, db)
    except NotFoundError:
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
        if item.appSessions != []:
            for app_session in item.appSessions:
                create_new_app_session(app_session, refreshed, db)
    finally:
        db.close()
    return new_entry


## function to read from the table
def read_db_product(item: CSLProduct, db: Session) -> CSLProduct:
    result = db.query(TblCSLProducts).filter(TblCSLProducts.id == item.id).first()
    if result is None:
        raise NotFoundError
    return result


## function to update the table
def update_db_product():
    pass


## function to delete from the table
def delete_db_product():
    pass
