"""Module that defines the result models for CSL Licenses"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from APICore.api_get_functions import get_all_x
from APICore.connection_models.collections import licenses
from APICore.connection_models.scopes import csl


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


## base function(s) for use with this model
def get_all_licenses() -> CSLLicenses:
    result = get_all_x(scope=csl, collection=licenses)
    return CSLLicenses.model_validate(result)
