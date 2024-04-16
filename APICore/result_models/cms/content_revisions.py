"""Module that defines the result models for CMS ContentRevisions"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


## creating the pydantic BaseModel
class CMSContentRevision(BaseModel):
    id: UUID
    contentId: UUID
    comment: Optional[str] | None = None
    revisedAt: datetime
    revisedById: UUID
    refreshedId: Optional[UUID] | None = None
