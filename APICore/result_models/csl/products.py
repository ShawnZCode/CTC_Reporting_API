"""Module that defines the result models for CSL Products"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from APICore.api_get_functions import get_all_x
from APICore.connection_models.collections import products
from APICore.connection_models.scopes import csl


## creating the pydantic BaseModel
class CSLProduct(BaseModel):
    id: UUID
    name: str


class CSLProducts(BaseModel):
    totalItems: int
    items: Optional[List[CSLProduct]] = []


## base function(s) for use with this model
def get_all_products() -> CSLProducts:
    result = get_all_x(scope=csl, collection=products)
    return CSLProducts.model_validate(result)
