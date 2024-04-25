"""Module that defines the result models for CMS Tags"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from APICore.api_get_functions import get_all_x, get_total_items, get_x_by_id
from APICore.connection_models.collections import tag, tags
from APICore.connection_models.scopes import cms
from APICore.result_models.cms.content_tags import CMSContentTag


## creating the pydantic BaseModel
class CMSTagBase(BaseModel):
    id: UUID
    addedAt: datetime
    addedById: UUID
    updatedAt: datetime
    updatedById: UUID
    name: str
    description: Optional[str] | None = None
    refreshedId: Optional[UUID] | None = None


class CMSTag(CMSTagBase):
    contentIds: Optional[List[UUID]] = []
    contentTags: Optional[List[CMSContentTag]] = []


class CMSTags(BaseModel):
    totalItems: int
    items: Optional[List[CMSTag]] = []


## base function(s) for use with this model
def get_all_tags() -> CMSTags:
    total_items = get_total_items(scope=cms, collection=tags)
    result = get_all_x(scope=cms, collection=tags, total_rows=total_items)
    return CMSTags.model_validate(result)


def get_tag_details_by_id(*, item: CMSTag) -> CMSTag:
    result = get_x_by_id(scope=cms, collection=tag, item_id=item.id)
    cms_tag = CMSTag.model_validate(result)
    if cms_tag.contentIds != []:
        cms_tag = create_content_tags(item=cms_tag)
    return cms_tag


def get_all_tag_details(objects: CMSTags) -> CMSTags:
    new_objects = CMSTags(totalItems=0, items=[])
    for item in objects.items:
        new_item = get_tag_details_by_id(item=item)
        new_objects.items.append(new_item)
        new_objects.totalItems = len(new_objects.items)
    return new_objects


def create_content_tags(item: CMSTag) -> CMSTag:
    for content_id in item.contentIds:
        ct = CMSContentTag.model_validate({"tagId": item.id, "contentId": content_id})
        item.contentTags.append(ct)
    return item
