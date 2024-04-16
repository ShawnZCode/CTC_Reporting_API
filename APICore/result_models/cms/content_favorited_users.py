"""Module that defines the result models for CMS ContentFavoritedUsers"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


## creating the pydantic BaseModel
class CMSContentFavoritedUser(BaseModel):
    userId: UUID
    refreshedId: Optional[UUID] | None = None
