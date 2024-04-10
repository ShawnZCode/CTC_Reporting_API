"""Module that defines the result models for Accounts Groups"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


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
