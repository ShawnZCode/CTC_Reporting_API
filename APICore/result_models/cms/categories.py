"""Module that defines the result models for CMS Categories"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


## creating the pydantic BaseModel
class CMSCategory(BaseModel):
    id: int
    name: str
    fileExtension: Optional[str] = None
    type: Optional[str] = None
    refreshedId: Optional[UUID] = None


class CMSCategories(BaseModel):
    totalItems: int
    items: Optional[List[CMSCategory]] = []
