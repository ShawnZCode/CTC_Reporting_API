from pydantic import BaseModel
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, Session, mapped_column

from APICore.result_models.accounts.roles import AccRole
from SQL_Connection.db_connection import Base, NotFoundError, SessionLocal


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblAccRoles(Base):
    __tablename__ = "roles"
    __table_args__ = {"schema": "accounts"}

    id: Mapped[int] = mapped_column(
        Integer(), primary_key=True, index=True, nullable=False
    )
    displayName: Mapped[str] = mapped_column(String(100), nullable=False)


## function to write to create a new entry item in the table
def write_db_role(
    item: AccRole,
    refreshed,
    session: Session = None,
) -> AccRole:
    db_item = TblAccRoles(**item.model_dump())
    if session is None:
        db = SessionLocal()
    else:
        db = session
    try:
        read_db_role(item, db)
    except NotFoundError:
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
    if session is None:
        db.close()
    return AccRole(**db_item.__dict__)


## function to read item from the table
def read_db_role(
    item: AccRole,
    session: Session = None,
) -> AccRole:
    if session is None:
        db = SessionLocal()
    else:
        db = session
    db_item = db.query(TblAccRoles).filter(TblAccRoles.id == item.id).first()
    if db_item is None:
        raise NotFoundError(f"UserId: {item.id} not found")
    if session is None:
        db.close()
    return AccRole(**db_item.__dict__)


## function to update the table
def update_db_role():
    pass


## function to read from the table
def get_all_roles():
    pass
