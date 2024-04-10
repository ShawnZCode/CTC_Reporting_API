"""Module that defines the result models for CMS Searches"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from APICore.result_models.cms.categories import CMSCategory


## creating the pydantic BaseModel
class CMSSearchBase(BaseModel):
    id: UUID
    totalExecutionTimeInMs: int
    hasExplicitLibraryFilter: bool
    minAvgRating: Optional[int] = None
    totalPageCount: int
    pageSize: int
    query: str
    totalResultCount: int
    savedSearchId: Optional[UUID] = None
    searchedAt: Optional[datetime] = None
    searchedById: Optional[UUID] = None
    searchId: Optional[UUID] = None
    fileVersions: Optional[List[str]] = []
    displayUnits: Optional[List[str]] = []
    sortBy: str
    sortDirection: str
    addedByUser: Optional[str] = None
    addedEndDate: Optional[datetime] = None
    addedStartDate: Optional[datetime] = None
    updatedByUser: Optional[str] = None
    updatedEndDate: Optional[datetime] = None
    updatedStartDate: Optional[datetime] = None
    refreshedId: Optional[UUID] = None


class CMSSearchCategory(BaseModel):
    searchId: UUID
    category: CMSCategory


class CMSSearchLibrary(BaseModel):
    searchId: UUID
    libraryId: UUID


class CMSSearchTag(BaseModel):
    searchId: UUID
    tagId: UUID


class CMSSearchSource(BaseModel):
    searchId: UUID
    contentSource: str


class CMSSearchResult(BaseModel):
    searchId: UUID
    contentId: UUID


class CMSSearchPage(BaseModel):
    id: UUID
    executionTimeInMs: int
    page: int
    pageSize: int
    resultCount: int
    results: Optional[List[CMSSearchResult]] = []


class CMSSearch(CMSSearchBase):
    sources: Optional[List[CMSSearchSource]] = []
    categories: Optional[List[CMSSearchCategory]] = []
    pages: Optional[List[CMSSearchPage]] = []
    searchLibraries: Optional[List[CMSSearchLibrary]] = []
    searchTags: Optional[List[CMSSearchTag]] = []


class CMSSearches(BaseModel):
    totalItems: int
    items: Optional[List[CMSSearch]] = []
