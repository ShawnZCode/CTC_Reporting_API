"""Module that defines the result models for PAL Sessions"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


## creating the pydantic BaseModel
class PALSession(BaseModel):
    id: UUID
    sessionId: UUID
    revitVersion: str
    userName: str
    machineName: str
    isOpen: bool
    logDate: datetime
    uploadDate: datetime
    addedDate: datetime
    rowVersion: str


class PALSessions(BaseModel):
    totalItems: int
    items: Optional[List[PALSession]] = []
