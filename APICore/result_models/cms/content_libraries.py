"""Module that defines the result models for CMS ContentLibraries"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


## creating the pydantic BaseModel
class CMSContentLibrary(BaseModel):
    libraryId: UUID
    contentId: UUID
    refreshedId: Optional[UUID] | None = None

    def __eq__(self, other) -> bool:
        if not isinstance(other, CMSContentLibrary):
            return NotImplemented
        return self.libraryId == other.libraryId and self.contentId == other.contentId
