"""Module that defines the result models for PAL Projects"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


## creating the pydantic BaseModel
class PALProjectBase(BaseModel):
    id: UUID
    projectNumber: str
    projectName: Optional[str] = None
    status: str
    office: Optional[str] = None
    buildingName: Optional[str] = None
    clientName: Optional[str] = None
    streetAddress: Optional[str] = None
    streetAddress2: Optional[str] = None
    streetAddress3: Optional[str] = None
    projectPhase: Optional[str] = None
    projectIssueDate: Optional[datetime] = None
    projectOwner: Optional[str] = None
    city: Optional[str] = None
    stateorProvince: Optional[str] = None
    postalCode: Optional[str] = None
    county: Optional[str] = None
    contact: Optional[str] = None
    addedDate: datetime
    addedByUserId: UUID
    updatedDate: datetime
    updatedByUserId: UUID


class PALProjectPath(BaseModel):
    id: UUID
    centralFilePath: str
    addedDate: datetime
    addedByUserId: UUID
    updatedDate: datetime
    updatedByUserId: UUID
    projectId: Optional[UUID] = None


class PALProjectPermission(BaseModel):
    id: UUID
    resourceId: UUID
    resourceType: str
    projectRole: str
    addedDate: datetime
    addedByUserId: UUID
    updatedDate: datetime
    updatedByUserId: UUID
    projectId: UUID


class PALProject(PALProjectBase):
    paths: Optional[List[PALProjectPath]] = []
    permissions: Optional[List[PALProjectPermission]] = []


class PALProjects(BaseModel):
    totalItems: int
    items: Optional[List[PALProject]] = []
