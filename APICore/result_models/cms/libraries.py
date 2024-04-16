"""Module that defines the result models for CMS Libraries"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from APICore.api_get_functions import get_all_x, get_total_items, get_x_by_id
from APICore.connection_models.collections import libraries, library
from APICore.connection_models.scopes import cms
from APICore.result_models.cms.library_permissions import (
    CMSLibraryPermission,
)


## creating the pydantic BaseModel
class CMSLibraryBase(BaseModel):
    id: UUID
    addedAt: datetime
    addedById: UUID
    updatedAt: datetime
    updatedById: UUID
    name: str
    type: str
    description: Optional[str] | None = None
    uploadContent: bool
    defaultRole: str
    imageUri: Optional[str] | None = None
    refreshedId: Optional[UUID] | None = None


class CMSLibrary(CMSLibraryBase):
    permissions: Optional[List[CMSLibraryPermission]] = []
    contentIds: Optional[List[UUID]] = []


class CMSLibraries(BaseModel):
    totalItems: int
    items: Optional[List[CMSLibrary]] = []


## base function(s) for use with this model
def get_all_libraries() -> CMSLibraries:
    total_items = get_total_items(scope=cms, collection=libraries)
    result = get_all_x(scope=cms, collection=libraries, total_rows=total_items)
    return CMSLibraries.model_validate(result)


def get_library_details_by_id(*, item: CMSLibrary) -> CMSLibrary:
    result = get_x_by_id(scope=cms, collection=library, item_id=item.id)
    return CMSLibrary.model_validate(result)


def get_all_library_details(objects: CMSLibraries) -> CMSLibraries:
    new_objects = CMSLibraries(totalItems=0, items=[])
    for item in objects.items:
        new_item = get_library_details_by_id(item=item)
        new_objects.items.append(new_item)
        new_objects.totalItems = len(new_objects.items)
    return new_objects
