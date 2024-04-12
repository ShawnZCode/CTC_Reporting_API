"""Module that defines the result models for CMS ContentFileComponentProperties"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


## creating the pydantic BaseModel
class CMSContentFileComponentProperty(BaseModel):
    id: UUID
    contentFileComponentId: Optional[UUID] = None
    isInstance: Optional[bool] = None
    isReadOnly: Optional[bool] = None
    name: str
    revitParameterGroupId: Optional[int] = None
    revitSharedParameterGuid: Optional[UUID] = None
    revitStorageTypeId: Optional[int] = None
    revitDisplayUnitTypeId: Optional[int] = None
    doubleValue: Optional[float] = None
    type: Optional[str] = None
    value: Optional[str] = None
    unitTypeIdVersionless: Optional[str] = None
    refreshedId: Optional[UUID] = None
