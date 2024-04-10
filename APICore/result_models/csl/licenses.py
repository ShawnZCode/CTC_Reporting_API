"""Module that defines the result models for CSL Licenses"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


## creating the pydantic BaseModel
class CSLLicenseBase(BaseModel):
    id: UUID
    productId: UUID
    productName: str
    serialNumber: str
    subscriptionStartDate: datetime
    subscriptionEndDate: datetime
    licenseCount: int
    licenseType: str
    autorenew: bool
    autorenewLicenseCount: int
    description: Optional[str]
    createdAt: datetime
    createdBy: UUID
    updatedAt: datetime
    updatedBy: UUID
    refreshedId: Optional[UUID] = None


class CSLLicensePermission(BaseModel):
    id: UUID
    resourceId: UUID
    resourceType: str
    assignedBy: UUID
    assignedAt: datetime


class CSLLicense(CSLLicenseBase):
    permissions: Optional[List[CSLLicensePermission]] = []


class CSLLicenses(BaseModel):
    totalItems: int
    items: Optional[List[CSLLicense]] = []
