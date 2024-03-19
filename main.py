"""Initialization import for nested references"""

# import os
import time
from shutil import rmtree

from JSON.create_json_cache_files import get_all_jsons

# SQL
from z_DB_API_Connector import main as GetTheStuff

# APICore
# from APICore_Connection.Functions import api_get_functions
# JSON


# Path Settings

# Testing Section for code
start_time = time.perf_counter()
container = GetTheStuff.last_refreshed.id
# container = "54fb64e1-de24-46d1-b017-03cff557eaa4"
GetTheStuff

# Cleanup the cached JSON files
rmtree(f"{GetTheStuff.root_path}/{container}", ignore_errors=True)

# get_all_jsons(container=container)
finish_time = time.perf_counter()
print(f"Finished in {round((finish_time-start_time)/60, 2)} minute(s)")
