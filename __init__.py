"""Initialization import for nested references"""

import time

#APICore
from APICore_Connection import api_get_functions

#JSON
#from JSON import read_file
from JSON.Classes import json_cache_files

#SQL
from SQL_Connection import sql_functions as sql

# Testing Section for code
start_time = time.perf_counter()

#sql.drop_database()
sql.connect_to_database()
sql.create_all_tables()
sql.write_tables_sequential()
#write_to_tables('Libraries', ctc.get_all_x('Libraries', ctc.get_total_items('Libraries')))

finish_time = time.perf_counter()
print(f'Finished in {round(finish_time-start_time, 2)} second(s)')
