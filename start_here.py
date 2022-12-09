"""Initialization import for nested references"""

import time

#APICore
#from APICore_Connection.Functions import api_get_functions

#JSON
#from JSON import read_file
from JSON.Functions import json_cache_files

#SQL
#from SQL_Connection.Functions import sql_functions as sql
from SQL_Connection.Classes.ctc_data_object import CTCDataObject
from SQL_Connection.Classes.ctc_database_connection import CTCDatabaseObject

# Testing Section for code
start_time = time.perf_counter()

#JSON Testing
#json_cache_files.get_base_jsons()

# sql.drop_database()
# with CTCDatabaseObject() as database_reset:
#     #print(database)
#     database_reset.database_delete()
#     #print(database)
#     database_reset = None
#     #print(database)
with CTCDatabaseObject() as database:
    #EnterData
    with CTCDataObject() as data:
        # TODO: Get data run through data object(s)
    #print(database, '\n', database.connection)


#sql.create_all_tables()
#sql.write_tables_sequential()
#write_to_tables('Libraries', ctc.get_all_x('Libraries', ctc.get_total_items('Libraries')))

finish_time = time.perf_counter()
print(f'Finished in {round(finish_time-start_time, 2)} second(s)')
