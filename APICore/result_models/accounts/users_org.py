"""Module that defines the result models for Accounts Users"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel

from APICore.api_get_functions import get_all_x
from APICore.connection_models.collections import users
from APICore.connection_models.scopes import accounts


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


## base function(s) for use with this model
def get_all_users() -> AccUsers:
    result = get_all_x(scope=accounts, collection=users)
    return AccUsers.model_validate(result)
