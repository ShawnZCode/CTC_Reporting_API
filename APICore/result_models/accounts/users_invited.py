"""Module that defines the result models for Accounts Invited Users"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


## creating the pydantic BaseModel
class AccInvitedUserBase(BaseModel):
    userId: UUID
    userName: str
    email: str
    isEnabled: bool
    invitationExpiration: datetime

    # refreshedId: Optional[UUID] = None


class AccLibraryPermission(BaseModel):
    libraryId: UUID
    role: str


class AccInvitedUser(AccInvitedUserBase):
    permissions: Optional[List[AccLibraryPermission]] = []


class AccInvitedUsers(BaseModel):
    totalItems: int
    items: Optional[List[AccInvitedUser]] = []
