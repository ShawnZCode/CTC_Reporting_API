"""Module that defines the result models for Core Refreshed"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel


## creating the pydantic BaseModel
class Refreshed(BaseModel):
    id: UUID = uuid4()
    refreshedAt: datetime = datetime.now()
