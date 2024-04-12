"""Module that defines the result models for CSL App Sessions"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field, PlainSerializer, WrapSerializer
from typing_extensions import Annotated

from APICore.api_get_functions import get_x_by_id
from APICore.connection_models.collections import app_sessions
from APICore.connection_models.scopes import csl
from APICore.result_models.csl.products import CSLProduct, CSLProducts


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
    sessionId: Optional[UUID] = None
    productId: UUID
    productName: Optional[str] = None
    productVersion: Optional[str] = None
    # startedAt: Optional[str] = None
    # endedAt: Optional[str] = None
    startedAt: Optional[CustomDateTime | datetime] = None
    endedAt: Optional[CustomDateTime | datetime] = None
    computerName: Optional[str] = None
    userId: Optional[UUID] = None
    applicationName: Optional[str] = None
    autodeskVersionNumber: Optional[str] = None
    autodeskSubVersionNumber: Optional[str] = None
    autodeskBuildNumber: Optional[str] = None


class CSLAppSessions(BaseModel):
    totalItems: int
    items: Optional[List[CSLAppSession]] = []


## base function(s) for use with this model
def get_app_session_details_by_product_id(*, item: CSLProduct) -> CSLAppSessions:
    result = get_x_by_id(scope=csl, collection=app_sessions, item_id=item.id)
    return CSLAppSessions.model_validate(result)


def get_all_app_session_details(*, objects: CSLProducts) -> CSLAppSessions:
    result = CSLAppSessions(totalItems=0, items=[])
    for item in objects.items:
        try:
            new_items = get_app_session_details_by_product_id(item=item)
            for new_item in new_items.items:
                if new_item.sessionId is None:
                    pass
                else:
                    result.items.append(new_item)
        except Exception as e:
            pass
        finally:
            result.totalItems = len(result.items)
    return result
