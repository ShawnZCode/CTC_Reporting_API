"""Module that defines the result models for PAL Document Sessions"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


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
    uploadDate: datetime
    addedDate: datetime


class PALLogAddIn(BaseModel):
    id: UUID
    name: str
    docSessionId: UUID
    logDate: datetime
    addedDate: datetime
    uploadedDate: datetime


class PALLogEvent(BaseModel):
    id: UUID
    docSessionId: UUID
    eventId: int
    eventType: Optional[str] = None
    eventName: Optional[str] = None
    viewName: Optional[str] = None
    viewId: Optional[str] = None
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
    addedDate: datetime
    uploadedDate: datetime


class PALLogLink(BaseModel):
    id: UUID
    docSessionId: UUID
    linkPath: str
    linkShortFileName: str
    linkType: str
    linkStatus: str
    logDate: datetime
    addedDate: datetime
    uploadedDate: datetime


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
    addedDate: datetime
    uploadedDate: datetime


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
    addedDate: datetime
    uploadedDate: datetime


class PALLogSummary(BaseModel):
    id: UUID
    docSessionId: UUID
    eventId: int
    groupCt: int
    inPlaceCt: int
    unPlacedCt: int
    unPlacedRoomCt: int
    unenclosedRoomCt: int
    placedRoomCt: int
    unPlacedSpaceCt: int
    unenclosedSpaceCt: int
    placedSpaceCt: int
    viewCt: int
    phaseCt: int
    desOptCt: int
    workesetCt: int
    familyCt: int
    instanceCt: int
    materialCt: int
    viewFilterCt: int
    unplacedFamilyCt: int
    levelCt: int
    warningCt: int
    warningTypeCt: int
    logDate: datetime
    addedDate: datetime
    uploadedDate: datetime


class PALLogViewType(BaseModel):
    id: UUID
    docSessionId: UUID
    viewTypeName: str
    viewCt: int
    logDate: datetime
    addedDate: datetime
    uploadedDate: datetime


class PALLogWarningSummary(BaseModel):
    id: UUID
    docSessionId: UUID
    warningCt: int
    description: str
    elementIds: str
    logDate: datetime
    addedDate: datetime
    uploadedDate: datetime


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
