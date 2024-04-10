"""Initialization import for nested references"""

import json

# import os
import time
from shutil import rmtree

# APICore
from APICore.result_models.accounts.users_org import AccUsers, get_all_users

# JSON
from JSON.create_json_cache_files import write_json_file

# SQL
# from z_DB_API_Connector import main as GetTheStuff


# Path Settings

# Testing Section for code
start_time = time.perf_counter()
# container = GetTheStuff.last_refreshed.id
# container = "54fb64e1-de24-46d1-b017-03cff557eaa4"
# GetTheStuff

users: AccUsers = get_all_users()
users_json = json.loads(users.model_dump_json())
write_json_file(stream=users_json, file_name="Users", sub_directory="Accounts")
# Cleanup the cached JSON files
# rmtree(f"{GetTheStuff.root_path}/{container}", ignore_errors=True)

# get_all_jsons(container=container)
finish_time = time.perf_counter()
print(f"Finished in {round((finish_time-start_time)/60, 2)} minute(s)")
