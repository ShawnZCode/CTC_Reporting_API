"""Module that defines the result models for CMS ContentLoads"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from APICore.result_models.cms.content_document import CMSContentDocument


## creating the pydantic BaseModel
class CMSContentLoadBase(BaseModel):
    id: UUID
    contentId: Optional[UUID] | None = None
    searchId: Optional[UUID] | None = None
    documentId: Optional[UUID] | None = None
    loadedAt: datetime
    loadedById: UUID
    refreshedId: Optional[UUID] | None = None

    def __eq__(self, other) -> bool:
        if not isinstance(other, CMSContentLoadBase):
            return NotImplemented
        return (
            self.id == other.id
            and self.loadedAt == other.loadedAt
            and self.contentId == other.contentId
            and self.documentId == other.documentId
        )


class CMSContentLoad(CMSContentLoadBase):
    document: Optional[CMSContentDocument] | None = None
