"""Initialization import for nested references"""

import time

from JSON.create_json_cache_files import CURRENT_DATE_TIME, get_all_jsons

if __name__ == "__main__":
    # Testing Section for code
    start_time = time.perf_counter()
    get_all_jsons(CURRENT_DATE_TIME)
    finish_time = time.perf_counter()
    print(f"Finished data fetch in {round((finish_time-start_time)/60, 2)} minute(s)")
