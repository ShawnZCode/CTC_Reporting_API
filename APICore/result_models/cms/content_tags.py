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
