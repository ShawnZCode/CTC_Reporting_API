"""Primary entry point for the API Core package."""

# APICore
from APICore.result_models.accounts.groups import AccGroups, get_all_groups
from APICore.result_models.accounts.roles import AccRoles, get_all_roles
from APICore.result_models.accounts.users_invited import (
    AccInvitedUsers,
    get_all_invited_users,
)
from APICore.result_models.accounts.users_org import AccUsers, get_all_users
from APICore.result_models.cms.contents import (
    CMSContents,
    get_all_content,
    get_all_content_details,
    get_content_details_by_id,
)
from APICore.result_models.cms.libraries import (
    CMSLibraries,
    get_all_libraries,
    get_all_library_details,
    get_library_details_by_id,
)
from APICore.result_models.cms.saved_searches import (
    CMSSavedSearches,
    get_all_saved_searches,
)
from APICore.result_models.cms.searches import (
    CMSSearches,
    get_all_search_details,
    get_all_searches,
    get_search_details_by_id,
)
from APICore.result_models.cms.tags import (
    CMSTags,
    get_all_tag_details,
    get_all_tags,
    get_tag_details_by_id,
)
from APICore.result_models.csl.app_sessions import (
    CSLAppSessions,
    get_all_app_session_details,
    get_app_session_details_by_product_id,
)
from APICore.result_models.csl.licenses import CSLLicenses, get_all_licenses
from APICore.result_models.csl.products import CSLProducts, get_all_products
from APICore.result_models.pal.doc_sessions import (
    PALDocSessions,
    get_all_doc_session_details,
    get_all_doc_sessions,
    get_doc_session_details_by_project_id,
)
from APICore.result_models.pal.projects import (
    PALProjects,
    get_all_project_details,
    get_all_projects,
    get_project_details_by_id,
)
from APICore.result_models.pal.sessions import (
    PALSessions,
    get_all_sessions,
)

# Constants

GET_FUNCTIONS = {
    "acc_users": get_all_users,
    "acc_invited_users": get_all_invited_users,
    "acc_groups": get_all_groups,
    "acc_roles": get_all_roles,
    "cms_libraries": get_all_libraries,
    "cms_saved_searches": get_all_saved_searches,
    "cms_searches": get_all_searches,
    "cms_tags": get_all_tags,
    "csl_products": get_all_products,
    "csl_licenses": get_all_licenses,
    "pal_sessions": get_all_sessions,
    "pal_projects": get_all_projects,
    "pal_doc_sessions": get_all_doc_sessions,
    "cms_contents": get_all_content,
}

GET_DETAILS_FUNCTIONS_ALL = {
    "cms_contents": get_all_content_details,
    "cms_libraries": get_all_library_details,
    "cms_searches": get_all_search_details,
    "cms_tags": get_all_tag_details,
    "csl_products": get_all_app_session_details,
    "pal_projects": get_all_project_details,
    "pal_doc_sessions": get_all_doc_session_details,
}
GET_DETAILS_FUNCTIONS_BY_ID = {
    "cms_contents": get_content_details_by_id,
    "cms_libraries": get_library_details_by_id,
    "cms_searches": get_search_details_by_id,
    "cms_tags": get_tag_details_by_id,
    "csl_products": get_app_session_details_by_product_id,
    "pal_projects": get_project_details_by_id,
    "pal_doc_sessions": get_doc_session_details_by_project_id,
}

# Automated Get Functions


def get_base_records(get_function):
    records = get_function()
    return records


def get_details(get_function, objects):
    records = get_function(objects=objects)
    return records


def get_details_by_id(get_function, object):
    record = get_function(item=object)
    return record
