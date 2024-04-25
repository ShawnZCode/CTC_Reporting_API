"""Initialization import for nested references"""

import time

from APICore.main import GET_DETAILS_FUNCTIONS_BY_ID, GET_FUNCTIONS
from SQL_Connection import tables
from SQL_Connection.db_connection import get_db

# from JSON.create_json_cache_files import CURRENT_DATE_TIME, get_all_jsons
from SQL_Connection.db_main import create_all, drop_all

TABLE_WRITE_FUNCTIONS = {
    "acc_users": tables.create_new_user,
    "acc_groups": tables.create_new_group,
    "cms_libraries": tables.create_new_library,
    "cms_contents": tables.create_new_content,
    "cms_tags": tables.create_new_tag,
}


def write_all_x(get_function, write_function, refreshed):
    """Write all data to the database"""
    collection_object = get_function()
    for item in collection_object.items:
        if get_function == GET_FUNCTIONS["cms_contents"]:
            item = GET_DETAILS_FUNCTIONS_BY_ID["cms_contents"](item=item)
        # if get_function == GET_FUNCTIONS["cms_libraries"]:
        #     item = GET_DETAILS_FUNCTIONS_BY_ID["cms_libraries"](item=item)
        write_function(item, refreshed)


if __name__ == "__main__":
    # Testing Section for code
    start_time = time.perf_counter()
    drop_all()
    create_all()
    new_refresh = tables.create_new_refreshed()
    for key, value in TABLE_WRITE_FUNCTIONS.items():
        write_all_x(GET_FUNCTIONS[key], value, new_refresh)
    # get_all_jsons(CURRENT_DATE_TIME)
    finish_time = time.perf_counter()
    print(f"Finished data fetch in {round((finish_time-start_time)/60, 2)} minute(s)")
