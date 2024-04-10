"""Module that defines the result models for CMS Tags"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


## creating the pydantic BaseModel
class CMSTagBase(BaseModel):
    id: UUID
    addedAt: datetime
    addedById: UUID
    updatedAt: datetime
    updatedById: UUID
    name: str
    description: str
    refreshedId: UUID


class CMSTag(CMSTagBase):
    contentIds: Optional[List[UUID]] = []


class CMSTags(BaseModel):
    totalItems: int
    items: Optional[List[CMSTag]] = []
