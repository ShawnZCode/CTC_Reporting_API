"""Initialization import for nested references"""

import time

# from JSON.create_json_cache_files import CURRENT_DATE_TIME, get_all_jsons
from SQL_Connection.db_main import create_all, drop_all, write_all

if __name__ == "__main__":
    # Testing Section for code
    start_time = time.perf_counter()
    # drop_all()
    # create_all()
    # write_all()
    # get_all_jsons(CURRENT_DATE_TIME)
    finish_time = time.perf_counter()
    print(f"Finished data fetch in {round((finish_time-start_time)/60, 2)} minute(s)")
