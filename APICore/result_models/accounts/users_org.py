"""Module that defines the result models for Accounts Users"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4

from pydantic import AliasChoices, BaseModel, Field

from APICore.api_get_functions import get_all_x, get_total_items
from APICore.connection_models.collections import users
from APICore.connection_models.scopes import accounts


## creating the pydantic BaseModel
class AccUserBase(BaseModel):
    id: UUID
    firstName: Optional[str] | None = None
    lastName: Optional[str] | None = None
    displayName: Optional[str] | None = None
    email: str
    description: Optional[str] | None = None
    office: Optional[str] = None
    department: Optional[str] | None = None
    lastLoggedInAt: Optional[datetime] | None = None
    status: str
    addedAt: datetime = Field(
        validation_alias=AliasChoices("createdAt", "addedAt"),
    )
    addedById: UUID = Field(
        validation_alias=AliasChoices(
            "addedBy",
            "addedById",
            "addedByUserId",
            "createdByUserId",
            "createdByUser",
            "createdById",
        )
    )
    updatedAt: datetime
    updatedById: UUID
    isSSOUser: bool
    refreshedId: Optional[UUID | None] = None

    def __eq__(self, other) -> bool:
        if not isinstance(other, AccUserBase):
            return NotImplemented
        return self.id == other.id and self.updatedAt == other.updatedAt


class AccUserRoles(BaseModel):
    userId: UUID
    roleId: int
    refreshedId: Optional[UUID] | None = None

    def __eq__(self, other) -> bool:
        if not isinstance(other, AccUserRoles):
            return NotImplemented
        return self.userId == other.userId and self.roleId == other.roleId


class AccUser(AccUserBase):
    roleAssignments: Optional[List[int]] = []
    userRoles: Optional[List[AccUserRoles]] = []


class AccUsers(BaseModel):
    totalItems: int
    items: Optional[List[AccUser]] = []


## base function(s) for use with this model
def get_all_users() -> AccUsers:
    total_items = get_total_items(scope=accounts, collection=users)
    result = get_all_x(scope=accounts, collection=users, total_rows=total_items)
    local_users = AccUsers.model_validate(result)
    for user in local_users.items:
        user = create_user_roles(user)
    return local_users


def create_user_roles(user: AccUser) -> AccUser:
    if user.roleAssignments != []:
        for role in user.roleAssignments:
            user_role = AccUserRoles(userId=user.id, roleId=role)
            user.userRoles.append(user_role)
    return user
