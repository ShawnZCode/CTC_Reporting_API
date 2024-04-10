"""module that defines the result models for CMS Content"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from APICore.result_models.cms.categories import CMSCategory
from APICore.result_models.cms.content_attachments import CMSContentAttachment
from APICore.result_models.cms.content_downloads import CMSContentDownload
from APICore.result_models.cms.content_favorited_users import CMSContentFavoritedUser
from APICore.result_models.cms.content_files import CMSContentFile
from APICore.result_models.cms.content_loads import CMSContentLoad
from APICore.result_models.cms.content_reviews import CMSContentReview
from APICore.result_models.cms.content_revisions import CMSContentRevision


## creating the pydantic BaseModel
class CMSContentBase(BaseModel):
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
    categoryId: Optional[int] = None
    previewImageUri: Optional[str] = None
    displayUnit: Optional[str] = None
    revitFamilyHostType: Optional[str] = None
    refreshedId: Optional[UUID] = None


class CMSContent(CMSContentBase):
    category: Optional[CMSCategory] = []
    contentFiles: Optional[CMSContentFile] = []
    contentAttachments: Optional[List[CMSContentAttachment]] = []
    contentDownlaods: Optional[List[CMSContentDownload]] = []
    contentLoads: Optional[List[CMSContentLoad]] = []
    contentReviews: Optional[List[CMSContentReview]] = []
    contentRevisions: Optional[List[CMSContentRevision]] = []
    contentTagIds: Optional[List[UUID]] = []
    contentLibraryIds: Optional[List[UUID]] = []
    favoritedUsers: Optional[List[CMSContentFavoritedUser]] = []


class CMSContents(BaseModel):
    totalItems: int
    items: Optional[List[CMSContent]] = []
