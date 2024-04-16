"""Module that defines the result models for PAL Projects"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import AliasChoices, BaseModel, Field

from APICore.api_get_functions import get_all_x, get_total_items, get_x_by_id
from APICore.connection_models.collections import project, projects
from APICore.connection_models.scopes import pal


## creating the pydantic BaseModel
class PALProjectBase(BaseModel):
    id: UUID
    projectNumber: str
    projectName: Optional[str] | None = None
    status: str
    office: Optional[str] | None = None
    buildingName: Optional[str] | None = None
    clientName: Optional[str] | None = None
    streetAddress: Optional[str] | None = None
    streetAddress2: Optional[str] | None = None
    streetAddress3: Optional[str] | None = None
    projectPhase: Optional[str] | None = None
    projectIssueDate: Optional[datetime] | None = None
    projectOwner: Optional[str] | None = None
    city: Optional[str] | None = None
    stateorProvince: Optional[str] | None = None
    postalCode: Optional[str] | None = None
    county: Optional[str] | None = None
    contact: Optional[str] | None = None
    addedAt: datetime = Field(
        validation_alias=AliasChoices(
            "addedAt",
            "addedDate",
        )
    )
    addedById: UUID = Field(
        validation_alias=AliasChoices(
            "addedBy",
            "addedById",
            "addedByUserId",
        )
    )
    updatedAt: datetime = Field(
        validation_alias=AliasChoices(
            "updatedAt",
            "updatedDate",
        )
    )
    updatedById: UUID = Field(
        validation_alias=AliasChoices(
            "updatedBy",
            "updatedById",
            "updatedByUserId",
        )
    )


class PALProjectPath(BaseModel):
    id: UUID
    centralFilePath: str
    addedAt: datetime = Field(
        validation_alias=AliasChoices(
            "addedAt",
            "addedDate",
        )
    )
    addedById: UUID = Field(
        validation_alias=AliasChoices(
            "addedBy",
            "addedById",
            "addedByUserId",
        )
    )
    updatedAt: datetime = Field(
        validation_alias=AliasChoices(
            "updatedAt",
            "updatedDate",
        )
    )
    updatedById: UUID = Field(
        validation_alias=AliasChoices(
            "updatedBy",
            "updatedById",
            "updatedByUserId",
        )
    )
    projectId: Optional[UUID] = None


class PALProjectPermission(BaseModel):
    id: UUID
    resourceId: UUID
    resourceType: str
    projectRole: str
    addedAt: datetime = Field(
        validation_alias=AliasChoices(
            "addedAt",
            "addedDate",
        )
    )
    addedById: UUID = Field(
        validation_alias=AliasChoices(
            "addedBy",
            "addedById",
            "addedByUserId",
        )
    )
    updatedAt: datetime = Field(
        validation_alias=AliasChoices(
            "updatedAt",
            "updatedDate",
        )
    )
    updatedById: UUID = Field(
        validation_alias=AliasChoices(
            "updatedBy",
            "updatedById",
            "updatedByUserId",
        )
    )
    projectId: UUID


class PALProject(PALProjectBase):
    projectPaths: Optional[List[PALProjectPath]] = []
    projectPermissions: Optional[List[PALProjectPermission]] = []


class PALProjects(BaseModel):
    totalItems: int
    items: Optional[List[PALProject]] = []


## base function(s) for use with this model
def get_all_projects() -> PALProjects:
    total_items = get_total_items(scope=pal, collection=projects)
    result = get_all_x(scope=pal, collection=projects, total_rows=total_items)
    return PALProjects.model_validate(result)


def get_project_details_by_id(*, item: PALProject) -> PALProject:
    result = get_x_by_id(scope=pal, collection=project, item_id=item.id)
    return PALProject.model_validate(result)


def get_all_project_details(*, objects: PALProjects) -> PALProjects:
    new_objects = PALProjects(totalItems=0, items=[])
    for item in objects.items:
        new_item = get_project_details_by_id(item=item)
        new_objects.items.append(new_item)
        new_objects.totalItems = len(new_objects.items)
    return new_objects
