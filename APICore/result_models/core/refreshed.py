"""Module that defines the result models for Core Refreshed"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel


## creating the pydantic BaseModel
class Refreshed(BaseModel):
    id: UUID = uuid4()
    refreshStartedAt: datetime = datetime.now()
    refreshEndedAt: Optional[datetime] | None = None
    refreshDurationMinutes: Optional[int] | None = None

    def __eq__(self, other) -> bool:
        if not isinstance(other, Refreshed):
            return NotImplemented
        return self.id == other.id and self.refreshStartedAt == other.refreshStartedAt
