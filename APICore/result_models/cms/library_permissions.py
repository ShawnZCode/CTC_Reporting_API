"""Module that defines the result models for CMS Library Permissions"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


## creating the pydantic BaseModel
class CMSLibraryPermission(BaseModel):
    id: UUID
    libraryId: UUID
    librarySubscriptionId: Optional[UUID] | None = None
    resourceId: UUID
    resourceType: str
    resourceSource: str
    role: str
    addedAt: datetime
    addedById: UUID
    updatedAt: datetime
    updatedById: UUID
    refreshedId: Optional[UUID] | None = None

    def __eq__(self, other) -> bool:
        if not isinstance(other, CMSLibraryPermission):
            return NotImplemented
        return (
            self.id == other.id
            and self.updatedAt == other.updatedAt
            and self.libraryId == other.libraryId
        )
