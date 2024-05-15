"""Module that defines the result models for CMS ContentFavoritedUsers"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


## creating the pydantic BaseModel
class CMSContentFavoritedUser(BaseModel):
    userId: UUID
    contentId: Optional[UUID] | None = None
    refreshedId: Optional[UUID] | None = None

    def __eq__(self, other) -> bool:
        if not isinstance(other, CMSContentFavoritedUser):
            return NotImplemented
        return self.userId == other.userId and self.contentId == other.contentId
