"""module that defines the result models for CMS ContentFileComponentProperties"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


## creating the pydantic BaseModel
class CMSContentFileComponentProperty(BaseModel):
    id: UUID
    contentFileComponentId: UUID
    isinstance: bool
    isReadOnly: bool
    name: str
    revirParameterGroupId: int
    revitSharedParameterGuid: UUID
    revitStorageTypeId: int
    revitDisplayUnitTypeId: int
    doubleValue: float
    type: int
    value: str
    unitTypeIdVersionless: str
    refreshedId: UUID
