"""module that defines the result models for CMS ContentFiles"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from APICore.result_models.cms.contentFileComponents import CMSContentFileComponent


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
    fileSizeinBytes: int
    fileCreatedAt: datetime
    fileModifiedAt: datetime
    fileVersion: int
    contentId: UUID
    hasRevitTypeCatalog: bool
    revitSourceProjectElementId: int
    revitContainerProjectElementId: int
    revitProjectWorksharingMode: int
    location: str
    refreshedId: Optional[UUID] = None


class CMSContentFile(CMSContentFileBase):
    contentFileComponents: Optional[CMSContentFileComponent] = None
