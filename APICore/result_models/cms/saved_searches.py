"""Module that defines the result models for CMS Saved-Searches"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from APICore.api_get_functions import get_all_x, get_total_items, get_x_by_id
from APICore.connection_models.collections import saved_searches
from APICore.connection_models.scopes import cms
from APICore.result_models.cms.searches import CMSSearchBase


## creating the pydantic BaseModel
class CMSSavedSearchBase(CMSSearchBase):
    id: UUID
    name: str
    description: Optional[str] | None = None
    scope: Optional[str] | None = None
    addedAt: datetime
    addedById: UUID
    updatedAt: datetime
    updatedById: UUID


class CMSSavedSearches(BaseModel):
    totalItems: int
    items: Optional[List[CMSSavedSearchBase]] = []


## base function(s) for use with this model
def get_all_saved_searches() -> CMSSavedSearches:
    total_items = get_total_items(scope=cms, collection=saved_searches)
    result = get_all_x(scope=cms, collection=saved_searches, total_rows=total_items)
    return CMSSavedSearches.model_validate(result)
