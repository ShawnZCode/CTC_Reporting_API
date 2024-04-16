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
    fileExtension: Optional[str] | None = None
    fileSizeinBytes: Optional[int] | None = None
    contentId: UUID
    description: Optional[str] | None = None
    isLink: bool
    name: str
    path: Optional[str] | None = None
    type: Optional[str] | None = None
    refreshedId: Optional[UUID] | None = None
