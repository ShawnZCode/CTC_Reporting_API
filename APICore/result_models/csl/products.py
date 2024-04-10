"""Module that defines the result models for CSL Products"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


## creating the pydantic BaseModel
class CSLProduct(BaseModel):
    id: UUID
    name: str


class CSLProducts(BaseModel):
    totalItems: int
    items: Optional[List[CSLProduct]] = []
