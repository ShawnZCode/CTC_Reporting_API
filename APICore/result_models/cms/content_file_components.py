"""Module that defines the result models for CMS ContentFileComponents"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from APICore.result_models.cms.content_file_component_properties import (
    CMSContentFileComponentProperty,
)


## creating the pydantic BaseModel
class CMSContentFileComponentBase(BaseModel):
    id: UUID
    contentFileId: Optional[UUID] | None = None
    name: str
    refreshedId: Optional[UUID] | None = None

    def __eq__(self, other) -> bool:
        if not isinstance(other, CMSContentFileComponentBase):
            return NotImplemented
        return self.id == other.id and self.contentFileId == other.contentFileId


class CMSContentFileComponent(CMSContentFileComponentBase):
    properties: Optional[List[CMSContentFileComponentProperty]] = []
