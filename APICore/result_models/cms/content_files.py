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
    fileVersion: Optional[int] = None
    contentId: Optional[UUID] = None
    hasRevitTypeCatalog: Optional[bool] = None
    revitSourceProjectElementId: Optional[int] = None
    revitContainerProjectElementId: Optional[int] = None
    revitProjectWorksharingMode: Optional[int] = None
    location: str
    refreshedId: Optional[UUID] = None


class CMSContentFile(CMSContentFileBase):
    components: Optional[List[CMSContentFileComponent]] = None
