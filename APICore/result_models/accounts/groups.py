"""Module that defines the result models for Accounts Groups"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from APICore.api_get_functions import get_all_x
from APICore.connection_models.collections import groups
from APICore.connection_models.scopes import accounts


## creating the pydantic BaseModel
class AccGroupBase(BaseModel):
    id: UUID
    name: str
    description: Optional[str]
    createdAt: datetime
    createdByUserId: UUID
    updatedAt: datetime
    updatedByUserId: UUID
    isDefaultGroup: bool
    # refreshedId: UUID


class AccGroup(AccGroupBase):
    roleAssignments: Optional[List[int]] = []
    memberIds: Optional[List[UUID]] = []


class AccGroups(BaseModel):
    totalItems: int
    items: Optional[List[AccGroup]] = []


## base function(s) for use with this model
def get_all_groups() -> AccGroups:
    result = get_all_x(scope=accounts, collection=groups)
    return AccGroups.model_validate(result)
