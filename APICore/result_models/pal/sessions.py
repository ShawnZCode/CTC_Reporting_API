"""Module that defines the result models for PAL Sessions"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import AliasChoices, BaseModel, Field

from APICore.api_get_functions import get_all_x, get_total_items
from APICore.connection_models.collections import sessions
from APICore.connection_models.scopes import pal


## creating the pydantic BaseModel
class PALSession(BaseModel):
    id: UUID
    sessionId: UUID
    revitVersion: Optional[str | int] | None = None
    userName: str
    machineName: str
    isOpen: bool
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
    refreshedId: Optional[UUID] | None = None


class PALSessions(BaseModel):
    totalItems: int
    items: Optional[List[PALSession]] = []


## defining the get functions
def get_all_sessions(*, start_date: str | None = None) -> PALSessions:
    total_items = get_total_items(
        scope=pal,
        collection=sessions,
        start_date=start_date,
    )
    result = get_all_x(
        scope=pal,
        collection=sessions,
        total_rows=total_items,
        start_date=start_date,
    )
    return PALSessions.model_validate(result)
