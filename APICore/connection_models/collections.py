"""This module contains the defined models for the Collections in the APICore_Connection app."""

from APICore.connection_models.base import Collection

# Collections and Scopes for Accounts used in the Reporting API
users: Collection = Collection(
    name="users",
    optional_switches=[
        {"orderBy": "displayName"},
        {"orderDescending": False},
    ],
)

invited_users: Collection = Collection(
    name="invited-users",
    optional_switches=[
        {"includeInvLibraries": True},
        {"orderBy": "displayName"},
        {"orderDescending": False},
    ],
)

groups: Collection = Collection(
    name="groups",
    optional_switches=[
        {"orderBy": "Name"},
        {"orderDescending": False},
    ],
)

role_values: Collection = Collection(name="role-values")


# Collections for CMS used in the Reporting API
contents: Collection = Collection(
    name="contents",
    optional_switches=[
        {"orderBy": "updatedAt"},
        {"orderDescending": True},
    ],
)

content: Collection = Collection(
    name="content",
    parent="contents",
    mandatory_switches=["contentId"],
    optional_switches=[
        {"includeFiles": True},
        {"includeTypes": False},
        {"includeTypeParameters": False},
        {"includeLibraries": True},
        # ^^ Unnecessry to include libraries since it is faster to get associations from the Libraries call
        {"includeAttachments": True},
        {"includeDownloads": True},
        {"includeLoads": True},
        {"includeDocuments": True},
        {"includeReviews": True},
        {"includeRevisions": True},
        {"includeTags": True},
        # ^^ Unnecessry to include tags since it is faster to get associations from the Tags call
        {"includeUsers": False},
        {"includeFavoritedUsers": True},
    ],
)

libraries: Collection = Collection(
    name="libraries",
    optional_switches=[
        {"orderBy": "updatedAt"},
        {"orderDescending": True},
    ],
)

library: Collection = Collection(
    name="library",
    parent="libraries",
    mandatory_switches=["libraryId"],
    optional_switches=[
        {"includePermissions": True},
        {"includeContents": True},
        {"includeUsers": False},
    ],
)

subscribed_libraries: Collection = Collection(
    name="subscribed-libraries",
    optional_switches=[
        {"orderBy": "subscribedAt"},
        {"orderDescending": True},
    ],
)

tags: Collection = Collection(
    name="tags",
    optional_switches=[
        {"orderBy": "updatedAt"},
        {"orderDescending": True},
    ],
)

tag: Collection = Collection(
    name="tag",
    parent="tags",
    mandatory_switches=["tagId"],
    optional_switches=[
        {"includeContents": True},
        {"includeUsers": False},
    ],
)

saved_searches: Collection = Collection(
    name="saved-searches",
    optional_switches=[
        {"orderBy": "updatedAt"},
        {"orderDescending": True},
    ],
)

searches: Collection = Collection(
    name="searches",
    optional_switches=[
        {"orderBy": "searchedAt"},
        {"orderDescending": True},
    ],
)

search: Collection = Collection(
    name="search",
    parent="searches",
    mandatory_switches=["searchId"],
    optional_switches=[
        {"includeResults": True},
        {"includeCategories": True},
        {"includeLibraries": True},
        {"includeTags": True},
        {"includeSources": True},
        {"includeUsers": False},
    ],
)


# Collections for CSL used in the Reporting API
licenses: Collection = Collection(
    name="licenses",
    optional_switches=[
        {"includePermissions": True},
        {"orderBy": "updatedAt"},
        {"orderDescending": True},
    ],
)

app_sessions: Collection = Collection(
    name="app-sessions",
    parent="products",
    mandatory_switches=["productId"],
    optional_switches=[
        {"orderBy": "updatedAt"},
        {"orderDescending": True},
    ],
)

products: Collection = Collection(
    name="products",
)


# Collections for PAL used in the Reporting API
doc_sessions: Collection = Collection(
    name="doc-sessions",
    optional_switches=[
        {"orderBy": "updatedAt"},
        {"orderDescending": True},
    ],
)

doc_session: Collection = Collection(
    name="doc-sesion",
    parent="doc-sessions",
    mandatory_switches=["sessionId"],
    optional_switches=[
        {"includeAddIns": True},
        {"includeCrashes": True},
        {"includeDocumentProjChanges": True},
        {"includeEvents": True},
        {"includeLinks": True},
        {"includeMachines": True},
        {"includePrints": True},
        {"includeSummaries": True},
        {"includeViewTypes": True},
        {"includeWarningSummaries": True},
        {"includeWarnings": False},
    ],
)

sessions: Collection = Collection(
    name="sessions",
    optional_switches=[
        {"orderBy": "logDate"},
        {"orderDescending": True},
    ],
)

projects: Collection = Collection(
    name="projects",
    optional_switches=[
        {"orderBy": "projectNumber"},
        {"orderDescending": True},
    ],
)

project: Collection = Collection(
    name="project",
    parent="projects",
    mandatory_switches=["projectId"],
    optional_switches=[
        {"orderBy": "logDate"},
        {"orderDescending": True},
    ],
)
