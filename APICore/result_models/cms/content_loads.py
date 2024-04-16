"""Module that defines the result models for CMS ContentLoads"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


## creating the pydantic BaseModel
class CMSContentLoad(BaseModel):
    id: UUID
    contentId: Optional[UUID] | None = None
    searchId: Optional[UUID] | None = None
    documentId: Optional[UUID] | None = None
    loadedAt: datetime
    loadedById: UUID
    refreshedId: Optional[UUID] | None = None
