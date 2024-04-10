from pydantic import BaseModel
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, Session, mapped_column

from APICore.result_models.accounts.roles import AccRole
from SQL_Connection.db_connection import Base, NotFoundError


## Using SQLAlchemy2.0 generate Table with association to the correct schema
class TblAccRoles(Base):
    __tablename__ = "roles"
    __table_args__ = {"schema": "accounts"}

    id: Mapped[int] = mapped_column(
        Integer(), primary_key=True, index=True, nullable=False
    )
    displayName: Mapped[str] = mapped_column(String(100), nullable=False)


## function to write to create a new entry item in the table
def create_new_role(item: AccRole, session: Session) -> AccRole:
    new_entry = TblAccRoles(**item.model_dump())
    session.add(new_entry)
    session.commit()
    session.refresh(new_entry)
    return new_entry


## function to read item from the table
def read_db_role(item: AccRole, session: Session) -> AccRole:
    db_user = session.query(TblAccRoles).filter(TblAccRoles.id == item.id).first()
    if db_user is None:
        raise NotFoundError(f"UserId: {item.id} not found")
    return db_user


## function to update the table
def update_user(item: AccRole, session: Session) -> AccRole:
    update_entry = read_db_role(item, session)
    if item.updatedAt.astimezone(None) > update_entry.updatedAt.astimezone(None):
        for key, value in item.model_dump().items():
            if key != "id":
                setattr(update_entry, key, value)
    session.commit()
    session.refresh(update_entry)
    return update_entry


## function to read from the table
def get_all_roles():
    pass
