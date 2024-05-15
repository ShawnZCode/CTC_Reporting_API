"""Module that defines the result models for Accounts Invited Users"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from APICore.api_get_functions import get_all_x, get_total_items
from APICore.connection_models.collections import invited_users
from APICore.connection_models.scopes import accounts


## creating the pydantic BaseModel
class AccInvitedUserBase(BaseModel):
    userId: UUID
    userName: str
    email: str
    isEnabled: bool
    invitationExpiration: datetime
    refreshedId: Optional[UUID] | None = None

    def __eq__(self, other) -> bool:
        if not isinstance(other, AccInvitedUserBase):
            return NotImplemented
        return (
            self.userId == other.userId
            and self.invitationExpiration == other.invitationExpiration
            and self.isEnabled == other.isEnabled
            and self.email == other.email
            and self.userName == other.userName
        )


class AccLibraryPermission(BaseModel):
    libraryId: UUID
    role: str

    def __eq__(self, other) -> bool:
        if not isinstance(other, AccLibraryPermission):
            return NotImplemented
        return self.libraryId == other.libraryId and self.role == other.role


class AccInvitedUser(AccInvitedUserBase):
    permissions: Optional[List[AccLibraryPermission]] = []


class AccInvitedUsers(BaseModel):
    totalItems: int
    items: Optional[List[AccInvitedUser]] = []


## base function(s) for use with this model
def get_all_invited_users() -> AccInvitedUsers:
    total_items = get_total_items(scope=accounts, collection=invited_users)
    result = get_all_x(scope=accounts, collection=invited_users, total_rows=total_items)
    return AccInvitedUsers.model_validate(result)
