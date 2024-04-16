"""Module that defines the result models for PAL Document Sessions"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import AliasChoices, BaseModel, Field

from APICore.api_get_functions import get_all_x, get_total_items, get_x_by_id
from APICore.connection_models.collections import doc_session, doc_sessions
from APICore.connection_models.scopes import pal


## creating the pydantic BaseModel
class PALDocSessionBase(BaseModel):
    id: UUID
    projectId: Optional[UUID] = None
    userName: str
    machineName: str
    server: Optional[str] = None
    centralFileName: str
    centralFilePath: str
    shortFileName: str
    localFileName: str
    localFileSize: int
    revitVersion: str
    isAudit: bool
    openingDuration: float
    worksetCt: int
    worksetEditCt: int
    worksetOpenCt: int
    basePoint: str
    surveyPoint: str
    angleToTrueNorth: float
    siteLatLong: str
    status: bool
    logDate: datetime
    uploadedAt: datetime = Field(
        validation_alias=AliasChoices(
            "uploadedAt",
            "uploadDate",
            "uploadedDate",
        )
    )
    addedAt: datetime = Field(
        validation_alias=AliasChoices(
            "addedAt",
            "addedDate",
        )
    )


class PALLogAddIn(BaseModel):
    id: UUID
    name: str
    docSessionId: UUID
    logDate: datetime
    addedAt: datetime = Field(
        validation_alias=AliasChoices(
            "addedAt",
            "addedDate",
        )
    )
    uploadedAt: datetime = Field(
        validation_alias=AliasChoices(
            "uploadedAt",
            "uploadDate",
            "uploadedDate",
        )
    )


class PALLogEvent(BaseModel):
    id: UUID
    docSessionId: UUID
    eventId: int
    eventType: Optional[str] = None
    eventName: Optional[str] = None
    viewName: Optional[str] = None
    viewId: Optional[int] = None
    openViewCt: int
    eventDuration: float
    actionCt: int
    activeWorksetName: Optional[str] = None
    familyWorksetOpenCt: Optional[int] = None
    familyWorksetEditCt: Optional[int] = None
    standardWorksetOpenCt: Optional[int] = None
    standardWorksetEditCt: Optional[int] = None
    userWorksetOpenCt: Optional[int] = None
    userWorksetEditCt: Optional[int] = None
    viewWorksetOpenCt: Optional[int] = None
    viewWorksetEditCt: Optional[int] = None
    logDate: datetime
    addedAt: datetime = Field(
        validation_alias=AliasChoices(
            "addedAt",
            "addedDate",
        )
    )
    uploadedAt: datetime = Field(
        validation_alias=AliasChoices(
            "uploadedAt",
            "uploadDate",
            "uploadedDate",
        )
    )


class PALLogLink(BaseModel):
    id: UUID
    docSessionId: UUID
    linkPath: str
    linkShortFileName: str
    linkType: str
    linkStatus: str
    logDate: datetime
    addedAt: datetime = Field(
        validation_alias=AliasChoices(
            "addedAt",
            "addedDate",
        )
    )
    uploadedAt: datetime = Field(
        validation_alias=AliasChoices(
            "uploadedAt",
            "uploadDate",
            "uploadedDate",
        )
    )


class PALLogMachine(BaseModel):
    id: UUID
    docSessionId: UUID
    machineName: str
    processorId: str
    mac: str
    operatingSystem: str
    hdd: str
    motherboard: str
    bios: str
    ram: int
    slots: int
    cpu: str
    video: str
    ipaddress: str
    logDate: datetime
    addedAt: datetime = Field(
        validation_alias=AliasChoices(
            "addedAt",
            "addedDate",
        )
    )
    uploadedAt: datetime = Field(
        validation_alias=AliasChoices(
            "uploadedAt",
            "uploadDate",
            "uploadedDate",
        )
    )


class PALLogPrint(BaseModel):
    id: UUID
    docSessionId: UUID
    jobId: int
    userName: str
    printed: str
    failed: str
    printCt: int
    failCt: int
    jobStart: datetime
    jobEnd: datetime
    logDate: datetime
    addedAt: datetime = Field(
        validation_alias=AliasChoices(
            "addedAt",
            "addedDate",
        )
    )
    uploadedAt: datetime = Field(
        validation_alias=AliasChoices(
            "uploadedAt",
            "uploadDate",
            "uploadedDate",
        )
    )


class PALLogSummary(BaseModel):
    id: UUID
    docSessionId: UUID
    eventId: int
    groupCt: int
    inPlaceCt: int
    unPlacedCt: Optional[int] | None = None
    unPlacedRoomCt: int
    unenclosedRoomCt: int
    placedRoomCt: int
    unPlacedSpaceCt: int
    unenclosedSpaceCt: int
    placedSpaceCt: int
    viewCt: int
    phaseCt: int
    desOptCt: int
    worksetCt: int
    familyCt: int
    instanceCt: int
    materialCt: int
    viewFilterCt: int
    unplacedFamilyCt: int
    levelCt: int
    warningCt: int
    warningTypeCt: int
    logDate: datetime
    addedAt: datetime = Field(
        validation_alias=AliasChoices(
            "addedAt",
            "addedDate",
        )
    )
    uploadedAt: datetime = Field(
        validation_alias=AliasChoices(
            "uploadedAt",
            "uploadDate",
            "uploadedDate",
        )
    )


class PALLogViewType(BaseModel):
    id: UUID
    docSessionId: UUID
    viewTypeName: str
    viewCt: int
    logDate: datetime
    addedAt: datetime = Field(
        validation_alias=AliasChoices(
            "addedAt",
            "addedDate",
        )
    )
    uploadedAt: datetime = Field(
        validation_alias=AliasChoices(
            "uploadedAt",
            "uploadDate",
            "uploadedDate",
        )
    )


class PALLogWarningSummary(BaseModel):
    id: UUID
    docSessionId: UUID
    warningCt: int
    description: str
    elementIds: str
    logDate: datetime
    addedAt: datetime = Field(
        validation_alias=AliasChoices(
            "addedAt",
            "addedDate",
        )
    )
    uploadedAt: datetime = Field(
        validation_alias=AliasChoices(
            "uploadedAt",
            "uploadDate",
            "uploadedDate",
        )
    )


class PALDocSession(PALDocSessionBase):
    logAddIns: Optional[List[PALLogAddIn]] = []
    logEvents: Optional[List[PALLogEvent]] = []
    logLinks: Optional[List[PALLogLink]] = []
    logMachines: Optional[List[PALLogMachine]] = []
    logPrints: Optional[List[PALLogPrint]] = []
    logSummaries: Optional[List[PALLogSummary]] = []
    logViewTypes: Optional[List[PALLogViewType]] = []
    logWarningSummaries: Optional[List[PALLogWarningSummary]] = []


class PALDocSessions(BaseModel):
    totalItems: int
    items: Optional[List[PALDocSession]] = []


## base function(s) for use with this model
def get_all_doc_sessions() -> PALDocSessions:
    total_items = get_total_items(scope=pal, collection=doc_sessions)
    result = get_all_x(scope=pal, collection=doc_sessions, total_rows=total_items)
    return PALDocSessions.model_validate(result)


def get_doc_session_details_by_project_id(*, item: PALDocSession) -> PALDocSession:
    result = get_x_by_id(scope=pal, collection=doc_session, item_id=item.id)
    return PALDocSession.model_validate(result)


def get_all_doc_session_details(*, objects: PALDocSessions) -> PALDocSessions:
    new_objects = PALDocSessions(totalItems=0, items=[])
    for item in objects.items:
        new_item = get_doc_session_details_by_project_id(item=item)
        new_objects.items.append(new_item)
        new_objects.totalItems = len(new_objects.items)
    return new_objects
