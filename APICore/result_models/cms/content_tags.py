"""Module that defines the result models for CMS contentTags"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


## creating the pydantic BaseModel
class CMSContentTag(BaseModel):
    contentId: UUID
    tagId: UUID
    refreshedId: Optional[UUID] | None = None

    def __eq__(self, other) -> bool:
        if not isinstance(other, CMSContentTag):
            return NotImplemented
        return self.contentId == other.contentId and self.tagId == other.tagId
