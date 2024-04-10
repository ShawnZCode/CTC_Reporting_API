"""Module that defines the result models for CMS Saved-Searches"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from APICore.result_models.cms.searches import CMSSearch


## creating the pydantic BaseModel
class CMSSavedSearchBase(CMSSearch):
    name: str
    description: Optional[str] = None
    scope: Optional[str] = None
    addedAt: datetime
    addedById: UUID
    updatedAt: datetime
    updatedById: UUID


class CMSSavedSearches(BaseModel):
    totalItems: int
    items: Optional[List[CMSSavedSearchBase]] = []
