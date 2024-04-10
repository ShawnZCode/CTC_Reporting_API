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
    contentFileId: UUID
    name: str
    refreshedId: UUID


class CMSContentFileComponent(CMSContentFileComponentBase):
    contentFileComponentProperties: Optional[List[CMSContentFileComponentProperty]] = (
        None
    )
