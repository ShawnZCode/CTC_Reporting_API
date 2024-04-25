"""Module that defines the result models for CSL Products"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from APICore.api_get_functions import get_all_x, get_total_items, get_x_by_id
from APICore.connection_models.collections import app_sessions, products
from APICore.connection_models.scopes import csl
from APICore.result_models.csl.app_sessions import CSLAppSession, CSLAppSessions


## creating the pydantic BaseModel
class CSLProductBase(BaseModel):
    id: UUID
    name: str


class CSLProduct(CSLProductBase):
    appSessions: Optional[List[CSLAppSession]] = []


class CSLProducts(BaseModel):
    totalItems: int
    items: Optional[List[CSLProduct]] = []


## base function(s) for use with this model
def get_all_products() -> CSLProducts:
    total_items = get_total_items(scope=csl, collection=products)
    result = get_all_x(scope=csl, collection=products, total_rows=total_items)
    return CSLProducts.model_validate(result)


def get_app_session_details_by_product_id(*, item: CSLProduct) -> CSLProduct:
    result = get_x_by_id(scope=csl, collection=app_sessions, item_id=item.id)
    local_app_sessions = CSLAppSessions.model_validate(result)
    item.appSessions = local_app_sessions.items
    return item


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


def get_all_product_app_sessions(objects: CSLProducts) -> CSLProducts:
    for product in objects.items:
        app_sessions = get_app_session_details_by_product_id(item=product)
        product.appSessions = app_sessions.items
    return objects
