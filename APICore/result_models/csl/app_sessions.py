"""Module that defines the result models for CSL App Sessions"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


## creating the pydantic BaseModel
class CSLAppSession(BaseModel):
    sessionId: UUID
    productId: UUID
    productName: str
    productVersion: Optional[str] = None
    startedAt: datetime
    endedAt: Optional[datetime] = None
    computerName: str
    userId: UUID
    applicationName: str
    autodeskVersionNumber: Optional[str] = None
    autodeskSubVersionNumber: Optional[str] = None
    autodeskBuildNumber: Optional[str] = None


class CSLAppSessions(BaseModel):
    totalItems: int
    items: Optional[List[CSLAppSession]] = []
