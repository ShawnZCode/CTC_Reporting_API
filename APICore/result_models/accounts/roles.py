"""Module that defines the result models for Accounts Roles"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import AliasChoices, BaseModel, Field

from APICore.api_get_functions import get_all_x
from APICore.connection_models.collections import role_values
from APICore.connection_models.scopes import accounts


## creating the pydantic BaseModel
class AccRole(BaseModel):
    id: int = Field(validation_alias=AliasChoices("intValue", "id"))
    displayName: str


class AccRoles(BaseModel):
    totalItems: int
    items: Optional[List[AccRole]] = []


## base function(s) for use with this model
def get_all_roles() -> AccRoles:
    result = get_all_x(scope=accounts, collection=role_values)
    return AccRoles.model_validate(result)
