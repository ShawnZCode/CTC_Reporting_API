"""Initialization import for nested references"""

import json

# import os
import time
from shutil import rmtree

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
)
from APICore.result_models.cms.libraries import (
    CMSLibraries,
    get_all_libraries,
    get_all_library_details,
)
from APICore.result_models.cms.saved_searches import (
    CMSSavedSearches,
    get_all_saved_searches,
)
from APICore.result_models.cms.searches import (
    CMSSearches,
    get_all_search_details,
    get_all_searches,
)
from APICore.result_models.cms.tags import (
    CMSTags,
    get_all_tag_details,
    get_all_tags,
)
from APICore.result_models.csl.app_sessions import (
    CSLAppSessions,
    get_all_app_session_details,
)
from APICore.result_models.csl.licenses import CSLLicenses, get_all_licenses
from APICore.result_models.csl.products import CSLProducts, get_all_products

# JSON
from JSON.create_json_cache_files import write_json_file

# SQL
# from z_DB_API_Connector import main as GetTheStuff

# Constants

GET_FUNCTIONS = {
    "acc_users": get_all_users,
    "acc_invited_users": get_all_invited_users,
    "acc_groups": get_all_groups,
    "acc_roles": get_all_roles,
    "cms_contents": get_all_content,
    "cms_libraries": get_all_libraries,
    "cms_saved_searches": get_all_saved_searches,
    "cms_searches": get_all_searches,
    "cms_tags": get_all_tags,
    "csl_products": get_all_products,
    "csl_licenses": get_all_licenses,
}

GET_DETAILS_FUNCTIONS = {
    "cms_contents_details": get_all_content_details,
    "cms_libraries_details": get_all_library_details,
    "cms_searches_details": get_all_search_details,
    "cms_tags_details": get_all_tag_details,
    "csl_app_sessions_details": get_all_app_session_details,
}

# Path Settings

# Testing Section for code
start_time = time.perf_counter()
# container = GetTheStuff.last_refreshed.id
# container = "54fb64e1-de24-46d1-b017-03cff557eaa4"
# GetTheStuff


def get_collection_records(*, file_name: str, get_function):
    records = get_function()

    return records


def get_all_records():
    for key, value in GET_FUNCTIONS.items():
        records = get_collection_records(file_name=key, get_function=value)
        records_json = json.loads(records.model_dump_json())
        write_json_file(
            stream=records_json,
            file_name=key.title(),
            sub_directory="Base",
        )


def get_all_details(*, file_name: str, get_function, objects):
    records = get_function(objects=objects)
    records_json = json.loads(records.model_dump_json())
    write_json_file(
        stream=records_json, file_name=file_name.title(), sub_directory="Base"
    )


# get_all_records()

# Get the top X item details from the collection
collection = "csl_products"
item_quantity = 20
all_items = get_collection_records(
    file_name=collection,
    get_function=GET_FUNCTIONS[collection],
)

top_x_items = CSLProducts(
    totalItems=item_quantity,
    items=all_items.items[:item_quantity],
)
collection = "csl_app_sessions"
get_all_details(
    objects=top_x_items,
    file_name=collection,
    get_function=GET_DETAILS_FUNCTIONS[f"{collection}_details"],
)


# Cleanup the cached JSON files
# rmtree(f"{GetTheStuff.root_path}/{container}", ignore_errors=True)

# get_all_jsons(container=container)
finish_time = time.perf_counter()
print(f"Finished in {round((finish_time-start_time)/60, 2)} minute(s)")
