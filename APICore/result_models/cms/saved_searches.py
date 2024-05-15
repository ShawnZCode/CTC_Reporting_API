"""Module that defines the result models for CMS Saved-Searches"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from APICore.api_get_functions import get_all_x, get_total_items, get_x_by_id
from APICore.connection_models.collections import saved_searches
from APICore.connection_models.scopes import cms
from APICore.result_models.cms.searches import (
    CMSSearchCategory,
    CMSSearchLibrary,
    CMSSearchSource,
    CMSSearchTag,
)


## creating the pydantic BaseModel
class CMSSavedSearchBase(BaseModel):
    id: UUID
    name: str
    description: Optional[str] | None = None
    scope: Optional[str] | None = None
    addedAt: datetime
    addedById: UUID
    updatedAt: datetime
    updatedById: UUID
    minAvgRating: Optional[int] | None = None
    query: Optional[str] | None = None
    fileVersions: Optional[str] | None = None
    filterContentByNotTagged: bool = False
    displayUnits: Optional[str] | None = None
    sortBy: str
    sortDirection: str
    addedByUser: Optional[str] | None = None
    addedEndDate: Optional[datetime] | None = None
    addedStartDate: Optional[datetime] | None = None
    updatedByUser: Optional[str] | None = None
    updatedEndDate: Optional[datetime] | None = None
    updatedStartDate: Optional[datetime] | None = None
    refreshedId: Optional[UUID] | None = None

    def __eq__(self, other) -> bool:
        if not isinstance(other, CMSSavedSearchBase):
            return NotImplemented
        return self.id == other.id and self.updatedAt == other.updatedAt


class CMSSavedSearch(CMSSavedSearchBase):
    sources: Optional[List[CMSSearchSource]] = []
    categories: Optional[List[CMSSearchCategory]] = []
    searchLibraries: Optional[List[CMSSearchLibrary]] = []
    searchTags: Optional[List[CMSSearchTag]] = []


class CMSSavedSearches(BaseModel):
    totalItems: int
    items: Optional[List[CMSSavedSearch]] = []


## base function(s) for use with this model
def get_all_saved_searches() -> CMSSavedSearches:
    total_items = get_total_items(scope=cms, collection=saved_searches)
    result = get_all_x(scope=cms, collection=saved_searches, total_rows=total_items)
    return CMSSavedSearches.model_validate(result)
