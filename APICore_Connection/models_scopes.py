"""This module contains the defined models for the Scopes in the APICore_Connection app."""

import APICore_Connection.models_collections as collections
from APICore_Connection.models_base import Scope, Scopes

account_scope: Scope = Scope(
    name="accounts",
    collections=[
        collections.users,
        collections.groups,
        collections.role_values,
    ],
)

csl_scope: Scope = Scope(
    name="csl",
    collections=[
        collections.licenses,
        collections.app_sessions,
        collections.products,
    ],
)

cms_scope: Scope = Scope(
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

pal_scope: Scope = Scope(
    name="pal",
    collections=[
        collections.doc_sessions,
        collections.doc_sesion,
        collections.sessions,
        collections.projects,
        collections.project,
    ],
)

API_SCOPES: Scopes = Scopes(
    scopes=[
        account_scope,
        csl_scope,
        cms_scope,
        pal_scope,
    ]
)
