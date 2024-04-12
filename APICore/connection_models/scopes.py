"""This module contains the defined models for the Scopes in the APICore_Connection app."""

import APICore.connection_models.collections as collections
from APICore.connection_models.base import Scope, Scopes

accounts: Scope = Scope(
    name="accounts",
    collections=[
        collections.users,
        collections.groups,
        collections.role_values,
    ],
)

csl: Scope = Scope(
    name="csl",
    collections=[
        collections.licenses,
        collections.app_sessions,
        collections.products,
    ],
)

cms: Scope = Scope(
    name="cms",
    collections=[
        collections.contents,
        collections.content,
        collections.libraries,
        collections.library,
        collections.subscribed_libraries,
        collections.tags,
        collections.tag,
        collections.saved_searches,
        collections.searches,
        collections.search,
    ],
)

pal: Scope = Scope(
    name="pal",
    collections=[
        collections.doc_sessions,
        collections.doc_session,
        collections.sessions,
        collections.projects,
        collections.project,
    ],
)

API_SCOPES: Scopes = Scopes(
    scopes=[
        accounts,
        csl,
        cms,
        pal,
    ]
)
