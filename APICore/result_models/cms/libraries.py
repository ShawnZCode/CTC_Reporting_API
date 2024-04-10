"""Module that defines the result models for CMS Libraries"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from APICore.result_models.cms.library_permissions import (
    CMSLibraryPermission,
)


## creating the pydantic BaseModel
class CMSLibraryBase(BaseModel):
    id: UUID
    addedAt: datetime
    addedById: UUID
    updatedAt: datetime
    updatedById: UUID
    name: str
    type: str
    description: str
    uploadContent: bool
    defaultRole: str
    imageUri: str
    refreshedId: UUID


class CMSLibrary(CMSLibraryBase):
    permissions: Optional[List[CMSLibraryPermission]] = []
    contentIds: Optional[List[UUID]] = []


class CMSLibraries(BaseModel):
    totalItems: int
    items: Optional[List[CMSLibrary]] = []
