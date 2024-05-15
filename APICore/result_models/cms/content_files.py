"""Module that defines the result models for CMS ContentFiles"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from APICore.result_models.cms.content_file_components import CMSContentFileComponent


## creating the pydantic BaseModel
class CMSContentFileBase(BaseModel):
    id: UUID
    addedAt: datetime
    addedById: UUID
    updatedAt: datetime
    updatedById: UUID
    fileName: str
    filePath: str
    fileExtension: str
    fileSizeInBytes: int
    fileCreatedAt: datetime
    fileModifiedAt: datetime
    fileVersion: Optional[int] | None = None
    contentId: Optional[UUID] | None = None
    hasRevitTypeCatalog: Optional[bool] | None = None
    revitSourceProjectElementId: Optional[int] | None = None
    revitContainerProjectElementId: Optional[int] | None = None
    revitProjectWorksharingMode: Optional[int] | None = None
    location: str
    refreshedId: Optional[UUID] | None = None

    def __eq__(self, other) -> bool:
        if not isinstance(other, CMSContentFileBase):
            return NotImplemented
        return (
            self.id == other.id
            and self.updatedAt == other.updatedAt
            and self.contentId == other.contentId
        )


class CMSContentFile(CMSContentFileBase):
    components: Optional[List[CMSContentFileComponent]] = []
