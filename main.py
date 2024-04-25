"""Initialization import for nested references"""

import time

from APICore.main import GET_DETAILS_FUNCTIONS_BY_ID, GET_FUNCTIONS
from SQL_Connection import tables
from SQL_Connection.db_connection import get_db

# from JSON.create_json_cache_files import CURRENT_DATE_TIME, get_all_jsons
from SQL_Connection.db_main import create_all, drop_all

TABLE_WRITE_BASE = {
    "acc_users": tables.create_new_user,
    "acc_groups": tables.create_new_group,
    "csl_products": tables.create_new_product,
    "csl_licenses": tables.create_new_license,
    "cms_contents": tables.create_new_content,
    "cms_libraries": tables.create_new_library,
    "cms_tags": tables.create_new_tag,
    "cms_saved_searches": tables.create_new_saved_search,
    "cms_searches": tables.create_new_search,
}

TABLE_WRITE_DETAILS = {
    "cms_contents",
    "cms_libraries",
    "cms_tags",
    "cms_saved_searches",
    "cms_searches",
    "csl_products",
}


def write_all_x(key, refreshed):
    """Write all data to the database"""
    collection_object = GET_FUNCTIONS[key]()
    for item in collection_object.items:
        if key in TABLE_WRITE_DETAILS:
            item = GET_DETAILS_FUNCTIONS_BY_ID[key](item=item)
        TABLE_WRITE_BASE[key](item, refreshed)


if __name__ == "__main__":
    # Testing Section for code
    start_time = time.perf_counter()
    drop_all()
    create_all()
    new_refresh = tables.create_new_refreshed()
    for key in TABLE_WRITE_BASE.keys():
        write_all_x(key, new_refresh)
    # get_all_jsons(CURRENT_DATE_TIME)
    finish_time = time.perf_counter()
    print(f"Finished data fetch in {round((finish_time-start_time)/60, 2)} minute(s)")
