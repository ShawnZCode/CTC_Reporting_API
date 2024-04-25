"""Module that defines the result models for CSL App Sessions"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import AliasChoices, BaseModel, Field, PlainSerializer, WrapSerializer
from typing_extensions import Annotated


## creating custom datetime
def datetime_parser(date_string: str) -> datetime | None:
    if date_string == "":
        return None
    else:
        try:
            return_datetime: datetime = datetime(date_string)
        except:
            return_datetime: datetime = datetime.strptime(
                date_string, "%m/%d/%Y %I:%M:%S %p %z"
            )
    return return_datetime


CustomDateTime = Annotated[
    str,
    PlainSerializer(
        lambda s: datetime_parser(s),
        return_type=datetime | None,
    ),
]


## creating the pydantic BaseModel
class CSLAppSession(BaseModel):
    id: Optional[UUID] | None = Field(
        validation_alias=AliasChoices("sessionId"),
        default=None,
    )
    productId: UUID
    productName: Optional[str] | None = None
    productVersion: Optional[str] | None = None
    # startedAt: Optional[str] = None
    # endedAt: Optional[str] = None
    startedAt: Optional[CustomDateTime | datetime] | None = None
    endedAt: Optional[CustomDateTime | datetime] | None = None
    computerName: Optional[str] | None = None
    userId: Optional[UUID] | None = None
    applicationName: Optional[str] | None = None
    autodeskVersionNumber: Optional[str] | None = None
    autodeskSubVersionNumber: Optional[str] | None = None
    autodeskBuildNumber: Optional[str] | None = None


class CSLAppSessions(BaseModel):
    totalItems: int
    items: Optional[List[CSLAppSession]] = []
