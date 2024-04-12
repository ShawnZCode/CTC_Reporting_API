"""Module that defines the result models for CMS Searches"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import AliasChoices, BaseModel, Field

from APICore.api_get_functions import get_all_x, get_x_by_id
from APICore.connection_models.collections import search, searches
from APICore.connection_models.scopes import cms
from APICore.result_models.cms.content_categories import CMSCategory


## creating the pydantic BaseModel
class CMSSearchCategory(BaseModel):
    # searchId: Optional[UUID] = None
    category: CMSCategory


class CMSSearchLibrary(BaseModel):
    # searchId: UUID
    libraryId: UUID


class CMSSearchTag(BaseModel):
    # searchId: UUID
    searchId: UUID


class CMSSearchSource(BaseModel):
    # searchId: UUID
    contentSource: str


class CMSSearchResult(BaseModel):
    # searchId: UUID
    contentId: UUID


class CMSSearchPage(BaseModel):
    id: UUID
    executionTimeInMs: int
    page: int
    pageSize: int
    resultCount: int
    results: Optional[List[CMSSearchResult]] = []


class CMSSearchBase(BaseModel):
    id: UUID
    minAvgRating: Optional[int] = None
    query: Optional[str] = None
    fileVersions: Optional[str] = None
    displayUnits: Optional[List[str]] = []
    sortBy: str
    sortDirection: str
    addedByUser: Optional[str] = None
    addedEndDate: Optional[datetime] = None
    addedStartDate: Optional[datetime] = None
    updatedByUser: Optional[str] = None
    updatedEndDate: Optional[datetime] = None
    updatedStartDate: Optional[datetime] = None
    sources: Optional[List[CMSSearchSource]] = []
    categories: Optional[List[CMSSearchCategory]] = []
    searchLibraries: Optional[List[CMSSearchLibrary]] = []
    searchTags: Optional[List[CMSSearchTag]] = []
    refreshedId: Optional[UUID] = None


class CMSSearch(CMSSearchBase):
    searchId: Optional[UUID] = None
    savedSearchId: Optional[UUID] = None
    totalPageCount: int = Field(
        validation_alias=AliasChoices("totalPageCount", "totalPages"),
        default=None,
    )
    totalResultCount: int = Field(
        validation_alias=AliasChoices("totalResultCount", "totalResults"),
        default=None,
    )
    pageSize: Optional[int] = None
    searchedAt: Optional[datetime] = None
    searchedById: Optional[UUID] = None
    totalExecutionTimeInMs: int
    hasExplicitLibraryFilter: bool
    pages: Optional[List[CMSSearchPage]] = []


class CMSSearches(BaseModel):
    totalItems: int
    items: Optional[List[CMSSearch]] = []


## base function(s) for use with this model
def get_all_searches() -> CMSSearches:
    result = get_all_x(scope=cms, collection=searches)
    return CMSSearches.model_validate(result)


def get_search_details_by_id(*, item: CMSSearch) -> CMSSearch:
    result = get_x_by_id(scope=cms, collection=search, item_id=item.searchId)
    return CMSSearch.model_validate(result)


def get_all_search_details(objects: CMSSearches) -> CMSSearches:
    new_objects = CMSSearches(totalItems=0, items=[])
    for item in objects.items:
        new_item = get_search_details_by_id(item=item)
        new_objects.items.append(new_item)
        new_objects.totalItems = len(new_objects.items)
    return new_objects
