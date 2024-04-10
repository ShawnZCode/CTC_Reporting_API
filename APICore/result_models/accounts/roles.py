"""Module that defines the result models for Accounts Roles"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


## creating the pydantic BaseModel
class AccRole(BaseModel):
    id: int
    dispalyName: str


class AccRoles(BaseModel):
    totalItems: int
    items: Optional[List[AccRole]] = []
