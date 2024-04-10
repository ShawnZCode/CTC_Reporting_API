"""Module that defines the result models for Accounts Users"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


## creating the pydantic BaseModel
class AccUserBase(BaseModel):
    id: UUID
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    displayName: Optional[str] = None
    email: str
    description: Optional[str] = None
    office: Optional[str] = None
    department: Optional[str] = None
    lastLoggedInAt: Optional[datetime] = None
    status: str
    createdAt: datetime
    createdById: UUID
    updatedAt: datetime
    updatedById: UUID
    isSSOUser: bool
    # refreshedId: Optional[UUID] = None


class AccUser(AccUserBase):
    roles: Optional[list[int]] = []


class AccUsers(BaseModel):
    totalItems: int
    items: Optional[List[AccUser]] = []
