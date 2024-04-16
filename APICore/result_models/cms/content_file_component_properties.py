"""Module that defines the result models for CMS ContentFileComponentProperties"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


## creating the pydantic BaseModel
class CMSContentFileComponentProperty(BaseModel):
    id: UUID
    contentFileComponentId: Optional[UUID] | None = None
    isInstance: Optional[bool] | None = None
    isReadOnly: Optional[bool] | None = None
    name: str
    revitParameterGroupId: Optional[int] | None = None
    revitSharedParameterGuid: Optional[UUID] | None = None
    revitStorageTypeId: Optional[int] | None = None
    revitDisplayUnitTypeId: Optional[int] | None = None
    doubleValue: Optional[float] | None = None
    type: Optional[str] | None = None
    value: Optional[str] | None = None
    unitTypeIdVersionless: Optional[str] | None = None
    refreshedId: Optional[UUID] | None = None
