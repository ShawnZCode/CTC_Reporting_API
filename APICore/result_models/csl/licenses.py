"""Module that defines the result models for CSL Licenses"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import AliasChoices, BaseModel, Field

from APICore.api_get_functions import get_all_x, get_total_items
from APICore.connection_models.collections import licenses
from APICore.connection_models.scopes import csl


## creating the pydantic BaseModel
class CSLLicenseBase(BaseModel):
    id: UUID
    productId: UUID
    # productName: str
    serialNumber: str
    subscriptionStartDate: datetime
    subscriptionEndDate: datetime
    licenseCount: int
    licenseType: str
    autorenew: bool
    autorenewLicenseCount: int
    createdAt: datetime
    createdById: UUID = Field(
        validation_alias=AliasChoices(
            "createdBy",
            "createdById",
        ),
    )
    updatedAt: datetime
    updatedById: UUID = Field(
        validation_alias=AliasChoices(
            "updatedBy",
            "updatedById",
        ),
    )
    refreshedId: Optional[UUID] | None = None


class CSLLicensePermission(BaseModel):
    id: UUID
    resourceId: UUID
    resourceType: str
    addedById: UUID = Field(
        validation_alias=AliasChoices(
            "addedBy",
            "addedById",
            "addedByUserId",
            "assignedByUserId",
            "assignedByUser",
            "assignedById",
            "assignedBy",
        )
    )
    addedAt: datetime = Field(
        validation_alias=AliasChoices(
            "addedAt",
            "assignedAt",
        )
    )
    refreshedId: Optional[UUID] = None


class CSLLicense(CSLLicenseBase):
    permissions: Optional[List[CSLLicensePermission]] = []


class CSLLicenses(BaseModel):
    totalItems: int
    items: Optional[List[CSLLicense]] = []


## base function(s) for use with this model
def get_all_licenses() -> CSLLicenses:
    total_items = get_total_items(scope=csl, collection=licenses)
    result = get_all_x(scope=csl, collection=licenses, total_rows=total_items)
    return CSLLicenses.model_validate(result)
