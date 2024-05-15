"""Module that defines the result models for Accounts Groups"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import AliasChoices, BaseModel, Field

from APICore.api_get_functions import get_all_x, get_total_items
from APICore.connection_models.collections import groups
from APICore.connection_models.scopes import accounts


## creating the pydantic BaseModel
class AccGroupBase(BaseModel):
    id: UUID
    name: str
    description: Optional[str] | None = None
    addedAt: datetime = Field(
        validation_alias=AliasChoices("createdAt", "updatedAt"),
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
    updatedById: UUID = Field(
        validation_alias=AliasChoices(
            "updatedBy",
            "updatedById",
            "updatedByUserId",
        )
    )
    isDefaultGroup: bool
    refreshedId: Optional[UUID | None] = None

    def __eq__(self, other) -> bool:
        if not isinstance(other, AccGroupBase):
            return NotImplemented
        return self.id == other.id and self.updatedAt == other.updatedAt


class AccGroupMember(BaseModel):
    groupId: UUID
    memberId: UUID
    refreshedId: Optional[UUID] | None = None

    def __eq__(self, other) -> bool:
        if not isinstance(other, AccGroupMember):
            return NotImplemented
        return self.groupId == other.groupId and self.memberId == other.memberId


class AccGroupRole(BaseModel):
    groupId: UUID
    roleId: int
    refreshedId: Optional[UUID] | None = None

    def __eq__(self, other) -> bool:
        if not isinstance(other, AccGroupRole):
            return NotImplemented
        return self.groupId == other.groupId and self.roleId == other.roleId


class AccGroup(AccGroupBase):
    roleAssignments: Optional[List[int]] = []
    memberIds: Optional[List[UUID]] = []
    groupMembers: Optional[List[AccGroupMember]] = []
    groupRoles: Optional[List[AccGroupRole]] = []


class AccGroups(BaseModel):
    totalItems: int
    items: Optional[List[AccGroup]] = []


## base function(s) for use with this model
def get_all_groups() -> AccGroups:
    total_items = get_total_items(scope=accounts, collection=groups)
    result = get_all_x(scope=accounts, collection=groups, total_rows=total_items)
    local_groups = AccGroups.model_validate(result)
    for group in local_groups.items:
        group = create_group_roles(group)
        group = create_group_members(group)
    return local_groups


def create_group_roles(group: AccGroup) -> AccGroup:
    if group.roleAssignments != []:
        for role in group.roleAssignments:
            group_role = AccGroupRole(groupId=group.id, roleId=role)
            group.groupRoles.append(group_role)
    return group


def create_group_members(group: AccGroup) -> AccGroup:
    if group.memberIds != []:
        for member in group.memberIds:
            group_member = AccGroupMember(groupId=group.id, memberId=member)
            group.groupMembers.append(group_member)
    return group
