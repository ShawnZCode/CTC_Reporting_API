"""Module that defines the result models for CMS Searches"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import AliasChoices, BaseModel, Field

from APICore.api_get_functions import get_all_x, get_total_items, get_x_by_id
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
    id: UUID = Field(
        validation_alias=AliasChoices("searchId", "id"),
    )
    savedSearchId: Optional[UUID] | None = None
    query: Optional[str] | None = None
    sortBy: str
    sortDirection: str
    minAvgRating: Optional[int] | None = None
    addedByUser: Optional[str] | None = None
    addedEndDate: Optional[datetime] | None = None
    addedStartDate: Optional[datetime] | None = None
    updatedByUser: Optional[str] | None = None
    updatedEndDate: Optional[datetime] | None = None
    updatedStartDate: Optional[datetime] | None = None
    searchedAt: Optional[datetime] | None = None
    searchedById: Optional[UUID] | None = None
    totalExecutionTimeInMs: int
    totalPageCount: int | None = Field(
        validation_alias=AliasChoices("totalPageCount", "totalPages"),
        default=None,
    )
    pageSize: Optional[int] | None = None
    totalResultCount: int | None = Field(
        validation_alias=AliasChoices("totalResultCount", "totalResults"),
        default=None,
    )
    fileVersions: Optional[str] | None = None
    displayUnits: Optional[str] | None = None
    hasExplicitLibraryFilter: bool
    refreshedId: Optional[UUID] | None = None


class CMSSearch(CMSSearchBase):
    pages: Optional[List[CMSSearchPage]] = []
    sources: Optional[List[CMSSearchSource]] = []
    categories: Optional[List[CMSSearchCategory]] = []
    searchLibraries: Optional[List[CMSSearchLibrary]] = []
    searchTags: Optional[List[CMSSearchTag]] = []


class CMSSearches(BaseModel):
    totalItems: int
    items: Optional[List[CMSSearch]] = []


## base function(s) for use with this model
def get_all_searches(*, start_date: str | None = None) -> CMSSearches:
    total_items = get_total_items(
        scope=cms,
        collection=searches,
        start_date=start_date,
    )
    result = get_all_x(
        scope=cms,
        collection=searches,
        total_rows=total_items,
        start_date=start_date,
    )
    return CMSSearches.model_validate(result)


def get_search_details_by_id(*, item: CMSSearch) -> CMSSearch:
    if item.id is None:
        return item
    else:
        result = get_x_by_id(
            scope=cms,
            collection=search,
            item_id=item.id,
        )
        return CMSSearch.model_validate(result)


def get_all_search_details(*, objects: CMSSearches) -> CMSSearches:
    new_objects = CMSSearches(totalItems=0, items=[])
    for item in objects.items:
        new_item = get_search_details_by_id(item=item)
        new_objects.items.append(new_item)
        new_objects.totalItems = len(new_objects.items)
    return new_objects
