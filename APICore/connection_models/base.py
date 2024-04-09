"""This module contains the base model structures for the
APICore_Connection."""
from typing import Optional

from pydantic import BaseModel


class Collection(BaseModel):
    """Collection Model:

    name: is the name of the collection. It is expected that this will
    match the Reporting API endpoint.
    parent: is used to denote the 'name' of the immeadiate parent of the
    collection.
    mandatorySwitches: indicates any mandatory switches required by the
    Reporting API.
    optionalSwitches: indicates any optional switches that may be useful
    when calling the Reporting API.
    """

    name: str
    parent: Optional[str] = None
    mandatory_switches: Optional[list[str]] = None
    optional_switches: Optional[list[dict]] = None


class Scope(BaseModel):
    """Scope Model:

    name: is the name of the scope. It is expected that this will match
    the Reporting API scope.
    collections: is a list of Collection models that route through the
    specified scope.
    """

    name: str
    collections: list[Collection]


class Scopes(BaseModel):
    """Scopes Model:

    scopes: is a collection of Scope models.
    """

    scopes: list[Scope]
