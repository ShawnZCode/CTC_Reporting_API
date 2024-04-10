"""Module that defines the result models for CMS ContentAttachments"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


## creating the pydantic BaseModel
class CMSContentAttachment(BaseModel):
    id: UUID
    addedAt: datetime
    addedById: UUID
    updatedAt: datetime
    updatedById: UUID
    fileExtension: str
    fileSizeinBytes: int
    contentId: UUID
    description: str
    isLink: bool
    name: str
    path: str
    type: int
    refreshedId: UUID
