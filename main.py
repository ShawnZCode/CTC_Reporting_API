"""Initialization import for nested references"""

import time

# APICore
# from APICore_Connection.Functions import api_get_functions
from JSON.Functions import json_cache_files

# JSON
# from JSON.Functions import json_cache_files
from JSON.Functions.read_file import read_file

# from SQL_Connection.Classes.ctc_database_connection import CTCDatabaseObject

# SQL
# from SQL_Connection.Classes.ctc_query_object import CTCQueryObject

# Testing Section for code
start_time = time.perf_counter()


# JSON Testing
json_cache_files.get_base_jsons()

# sql.drop_database()
# with CTCDatabaseObject() as database_reset:
#     #print(database)
#     database_reset.database_delete()
#     #print(database)
#     database_reset = None
#     #print(database)
# with CTCDatabaseObject() as database:
#     #EnterData
#     sql_settings = read_file('SQL_Connection\\Settings.json')
#     sql_settings_db = sql_settings['databaseSettings']
#     for db_scope in sql_settings_db:
#         for table in sql_settings_db[db_scope]:
#             if '@' not in table \
#                 and 'TABLE' not in list(sql_settings_db[db_scope][table]['keysMap'].keys())[0]:
#                 query = CTCQueryObject(database.db_name,db_scope,sql_settings_db[db_scope][table]).query_insert
#                 print(query)
# table_name = sql_settings_db[db_scope][table]['sqlTableQuery']
# total_rows = api_get_functions.get_total_items(db_scope,table)
# json_stream = api_get_functions.get_all_x(table, db_scope, total_rows)


# sql.create_all_tables()
# sql.write_tables_sequential()
# write_to_tables('Libraries', ctc.get_all_x('Libraries', ctc.get_total_items('Libraries')))

finish_time = time.perf_counter()
print(f"Finished in {round((finish_time-start_time)/60, 2)} minute(s)")
