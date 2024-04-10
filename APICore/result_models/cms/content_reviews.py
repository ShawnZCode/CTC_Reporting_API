"""Module that defines the result models for CMS ContentReviews"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


## creating the pydantic BaseModel
class CMSContentReview(BaseModel):
    id: UUID
    contentId: UUID
    rating: int
    comment: str = None
    addedAt: datetime
    addedById: UUID
    updatedAt: datetime
    updatedById: UUID
    refreshedId: Optional[UUID] = None
