"""Module that defines the result models for CMS ContentDocuments"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


## creating the pydantic BaseModel
class CMSContentDocument(BaseModel):
    id: UUID
    fileName: str
    filePath: str
    type: str
    version: str | int | None = None
    revitCentralModelFilePath: Optional[str | None] = None
    revitWorksharingMode: Optional[str | None] = None
    refreshedId: Optional[UUID | None] = None
