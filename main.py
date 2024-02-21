"""Initialization import for nested references"""

import json
import time

from fastapi.params import Depends

# SQL
from sqlalchemy.orm import Session

from APICore_Connection.api_get_functions import get_all_x

# APICore
# from APICore_Connection.Functions import api_get_functions
# JSON
from JSON import create_json_cache_files
from JSON.read_file import read_file
from SQL_Connection.db_connection import NotFoundError, session_local
from SQL_Connection.db_main import create_all, drop_all
from SQL_Connection.Tables.tbl_acc_users import (
    Acc_User,
    Acc_UserRecord,
    Acc_UserRoles,
    create_new_user,
    read_db_user,
    update_user,
)
from SQL_Connection.Tables.tbl_core_refreshed import (
    Refreshed,
    create_new_refreshed,
    get_last_refreshed,
)

# Path Settings
root_path = read_file("JSON\\Settings.json")["files"]["storageCachePath"]

# Testing Section for code
start_time = time.perf_counter()


# JSON Testing


# SQL Testing
# drop_all()
create_all()


def create_user(content: Acc_User, db: Session) -> Acc_User:
    db_content = create_new_user(item=content, session=db)
    return Acc_User(**db_content.__dict__)


def create_update_users(last_refreshed_id: str):
    path = f"{root_path}/{last_refreshed_id}/Accounts/Users.json"
    contents = read_file(path)["items"]
    for content in contents:
        full_item = Acc_UserRecord(**content, roles=content["roleAssignments"])
        item = Acc_User(**full_item.model_dump())
        database = session_local()
        try:
            update_user(item=item, session=database)
            # create_roles(item, database)
        except NotFoundError:
            create_user(content=item, db=database)
        finally:
            database.close()


def create_refreshed():
    database = session_local()
    try:
        refreshed: Refreshed = create_new_refreshed(session=database)
    finally:
        database.close()
    return refreshed


def fetch_last_refreshed():
    database = session_local()
    try:
        refreshed: Refreshed = get_last_refreshed(session=database)
    finally:
        database.close()
    return refreshed


last_refreshed = create_refreshed()
# last_refreshed = fetch_last_refreshed()
create_json_cache_files.get_base_jsons(root=last_refreshed.id)
create_update_users(last_refreshed_id=last_refreshed.id)

finish_time = time.perf_counter()
print(f"Finished in {round((finish_time-start_time)/60, 2)} minute(s)")
