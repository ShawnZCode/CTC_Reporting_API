from sqlalchemy import DateTime, Uuid, String, Boolean, Float, Integer, ForeignKey
from uuid import UUID, uuid4
from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped
from SQL_Connection.db_connection import Base
from pydantic import BaseModel
from typing import Optional


## creating the 'groups' pydantic BaseModel
class Acc_Groups(BaseModel):
    id: UUID
    name: str
    description: Optional[str]
    createdAt: datetime
    createdBtId: UUID
    updatedAt: datetime
    updatedById: UUID
    isDefaultGroup: bool
    refreshedId: UUID

## Using SQLAlchemy2.0 generate 'groups' Table Creation with association to the 'accounts' schema
class Tbl_Acc_Groups(Base):
    __tablename__ = 'groups'
    __table_args__ = {"schema": "accounts"}

    id: Mapped[uuid4] = mapped_column(Uuid(), primary_key=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=True)
    createdAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    createdBtId: Mapped[uuid4] = mapped_column(ForeignKey('accounts.users.id'), nullable=False)
    updatedAt: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    updatedById: Mapped[uuid4] = mapped_column(ForeignKey('accounts.users.id'), nullable=False)
    isDefaultGroup: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    refreshedId: Mapped[uuid4] = mapped_column(ForeignKey('core.refreshed.id'), nullable=False)