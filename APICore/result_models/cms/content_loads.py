"""Module that defines the result models for CMS ContentLoads"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


## creating the pydantic BaseModel
class CMSContentLoad(BaseModel):
    id: UUID
    contentId: UUID
    searchId: UUID
    documentId: UUID
    loadedAt: datetime
    loadedById: UUID
    refreshedId: Optional[UUID] = None
