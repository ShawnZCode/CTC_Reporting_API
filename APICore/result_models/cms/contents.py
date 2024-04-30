"""module that defines the result models for CMS Content"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, ValidationError

from APICore.api_get_functions import get_all_x, get_total_items, get_x_by_id
from APICore.connection_models.collections import content, contents
from APICore.connection_models.scopes import cms
from APICore.result_models.cms.content_attachments import CMSContentAttachment
from APICore.result_models.cms.content_categories import CMSCategory
from APICore.result_models.cms.content_downloads import CMSContentDownload
from APICore.result_models.cms.content_favorited_users import CMSContentFavoritedUser
from APICore.result_models.cms.content_files import CMSContentFile
from APICore.result_models.cms.content_libraries import CMSContentLibrary
from APICore.result_models.cms.content_loads import CMSContentLoad
from APICore.result_models.cms.content_reviews import CMSContentReview
from APICore.result_models.cms.content_revisions import CMSContentRevision
from APICore.result_models.cms.content_tags import CMSContentTag
from APICore.result_models.local_base_model import LocalBaseModel


## creating the pydantic BaseModel
class CMSContentBase(LocalBaseModel):
    id: UUID
    addedAt: datetime
    addedById: UUID
    updatedAt: datetime
    updatedById: UUID
    name: str
    fileName: str
    fileExtension: str
    hasCustomPreviewImage: bool
    type: str
    source: str
    location: str
    averageRating: float
    categoryId: Optional[int] | None = None
    previewImageUri: Optional[str] | None = None
    displayUnit: Optional[str] | None = None
    revitFamilyHostType: Optional[str] | None = None
    refreshedId: Optional[UUID] | None = None


class CMSContent(CMSContentBase):
    category: Optional[CMSCategory] = []
    files: Optional[List[CMSContentFile]] = []
    contentAttachments: Optional[List[CMSContentAttachment]] = []
    downloads: Optional[List[CMSContentDownload]] = []
    loads: Optional[List[CMSContentLoad]] = []
    reviews: Optional[List[CMSContentReview]] = []
    revisions: Optional[List[CMSContentRevision]] = []
    contentTagIds: Optional[List[UUID]] = []
    contentTags: Optional[List[CMSContentTag]] = []
    contentLibraryIds: Optional[List[UUID]] = []
    contentLibraries: Optional[List[CMSContentLibrary]] = []
    favoritedUsers: Optional[List[CMSContentFavoritedUser]] = []


class CMSContents(LocalBaseModel):
    totalItems: int
    items: Optional[List[CMSContent]] = []


## base function(s) for use with this model
def get_all_content() -> CMSContents:
    total_items = get_total_items(scope=cms, collection=contents)
    result = get_all_x(scope=cms, collection=contents, total_rows=total_items)
    return CMSContents.model_validate(result)


def get_content_details_by_id(*, item: CMSContent) -> CMSContent:
    result = get_x_by_id(scope=cms, collection=content, item_id=item.id)
    try:
        cms_content = CMSContent.model_validate(result)
    except ValidationError:
        cms_content = None
        pass
    for file in cms_content.files:
        file.contentId = cms_content.id
        for comp in file.components:
            comp.contentFileId = file.id
            for prop in comp.properties:
                prop.contentFileComponentId = comp.id
    if cms_content.contentLibraryIds != []:
        cms_content = create_content_libraries(item=cms_content)
    if cms_content.contentTagIds != []:
        cms_content = create_content_tags(item=cms_content)
    return cms_content


def get_all_content_details(objects: CMSContents) -> CMSContents:
    new_objects = CMSContents(totalItems=0, items=[])
    for item in objects.items:
        new_item = get_content_details_by_id(item=item)
        if new_item is not None:
            new_objects.items.append(new_item)
        new_objects.totalItems = len(new_objects.items)
    return new_objects


def create_content_libraries(item: CMSContent) -> CMSContent:
    for library_id in item.contentLibraryIds:
        cl = CMSContentLibrary.model_validate(
            {"libraryId": library_id, "contentId": item.id}
        )
        item.contentLibraries.append(cl)
    return item


def create_content_tags(item: CMSContent) -> CMSContent:
    for tag_id in item.contentTagIds:
        ct = CMSContentTag.model_validate({"tagId": tag_id, "contentId": item.id})
        item.contentTags.append(ct)
    return item
