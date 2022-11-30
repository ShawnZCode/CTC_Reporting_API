"""General functions to connect with SQL server"""

#from asyncio.windows_events import NULL
from datetime import datetime
import time
#import json
import concurrent.futures as cf
from os import path
from getpass import getuser
import uuid
import pyodbc
import api_get_functions as ctc
from read_file import read_file

settings = read_file('Files\\SupportFiles\\Settings.json')

driver=settings['sql']['driver']
server=settings['sql']['server']
api_key=settings['CTCAPI']['reportKey']
db_name = f'CTC Reporting {api_key}'
database=db_name
uid=settings['sql']['uid']
pwd=settings['sql']['pwd']
uuid_current = ''

CONN_STR_1 = f'driver={driver};server={server};database={database};UID={uid};PWD={pwd};'
CONN_STR_2 = f'driver={driver};server={server};database=master;UID={uid};PWD={pwd};'

#QUERY_FILES_LIST controls the order of table creation
# and accesses the core SQL execution commands for table creation and
# Relationship building... Primarily used by 2 functions:
#    query_builder_tables and create_tables
QUERY_FILES_LIST = ['SQL\\!Base\\Refreshed'
                ,'SQL\\CMS\\Categories'
                #,'SQL\\CMS\\Categories_Data'
                ,'SQL\\CMS\\ContentAttachments'
                ,'SQL\\CMS\\ContentDownloads'
                ,'SQL\\CMS\\ContentFileComponentProperties'
                ,'SQL\\CMS\\ContentFileComponents'
                ,'SQL\\CMS\\ContentFiles'
                ,'SQL\\CMS\\ContentLibraries'
                ,'SQL\\CMS\\ContentLoads'
                ,'SQL\\CMS\\ContentReviews'
                ,'SQL\\CMS\\ContentRevisions'
                ,'SQL\\CMS\\Contents'
                ,'SQL\\CMS\\ContentTags'
                ,'SQL\\CMS\\Documents'
                ,'SQL\\CMS\\Feedbacks'
                ,'SQL\\CMS\\Libraries'
                ,'SQL\\CMS\\LibraryPermissions'
                ,'SQL\\CMS\\LibrarySubscriptions'
                ,'SQL\\CMS\\Saved-Searches'
                ,'SQL\\CMS\\SavedSearchCategories'
                ,'SQL\\CMS\\SavedSearchContentSources'
                ,'SQL\\CMS\\SavedSearchLibraries'
                ,'SQL\\CMS\\SavedSearchPermissions'
                ,'SQL\\CMS\\SavedSearchTags'
                ,'SQL\\CMS\\SearchContentSources'
                ,'SQL\\CMS\\Searches'
                ,'SQL\\CMS\\SearchLibraries'
                ,'SQL\\CMS\\SearchResults'
                ,'SQL\\CMS\\SearchCategories'
                ,'SQL\\CMS\\SearchTags'
                ,'SQL\\CMS\\Tags'
                ,'SQL\\CMS\\UserFavoriteContents'
                ,'SQL\\ORG\\Users'
                ,'SQL\\UPDATE_REFERENCES\\UpdateTables']

# base_files_dict is a JSON Stream that contains many settings for
# handling the data entry into SQL tables based on the nested sections
# within the API returned JSON stream for records by ID
base_file_dict = read_file('Files\\SupportFiles\\Files_Collection.json')
# base_tables_list is a list of the primary keys for the main tables
# from the base_file_dict stream, used when populating data into the
# primary tables
base_tables_list = base_file_dict.keys()

# fields is a stream that lists each table and related fields
# The order helps control the data entry order and is leveraged heavily
# by query_builder_tables and write_to_tables in the query building and
# data population functions
fields = read_file('Files\\SupportFiles\\Fields.json')

# Base data used to seed the categories table
# LIKELY DEPRECATED as base_file_dict is implemented
CSV = path.abspath('Files\\SupportFiles\\Categories.csv')
BASE_DATA_ENTRY = f"""BULK INSERT Categories
  FROM '{CSV}'
  WITH (FORMAT = 'CSV')"""

# Temporary testing parameter used to quickly fill a table with some base data
temp_values = read_file('Files\\z_StructureReference\\Contents.json')

def connect_to_server(connect_string=None):
    """Initiates the server connection using credentials
    ACCEPTS: connection string (Likely CONN_STR_1 or 2)
    RETURNS: A successful SQL Server connection or an error"""
    cs = connect_string # or localhost_connect_string
    try:
        con = pyodbc.connect(cs, autocommit=True)
        return con
    except Exception as err:
        return err

def connect_to_database(con_str_1=CONN_STR_1, con_str_2=CONN_STR_2):
    """Connects to the database or creates one if it doesn't exist
    ACCEPTS: 2 optional connection strings to be used in logic
    RETURNS: Successful database connection or an error"""
    try:
        # First attempt to connect directly to the database
        with connect_to_server(con_str_1) as con:
            with con.cursor() as cur:
                print('success')
            return con
    except Exception as err:
        # Second attempt to connect to server 'master' database
        # and create the the desired database
        con = connect_to_server(con_str_2)
        cur = con.cursor()
        # vvv Dedicated Database CREATE query
        query_1 = f"""CREATE database [{database}]
    CONTAINMENT = NONE
    ON  PRIMARY 
( NAME = N'{database}', FILENAME = N'C:\Program Files\Microsoft SQL server\MSSQL14.MSSQLserver\MSSQL\DATA\{database}.mdf' , SIZE = 5120KB , FILEGROWTH = 10%)
    LOG ON 
( NAME = N'{database}_log', FILENAME = N'C:\Program Files\Microsoft SQL server\MSSQL14.MSSQLserver\MSSQL\DATA\{database}_log.ldf' , SIZE = 1024KB , FILEGROWTH = 10%)"""
        # vvv Dedicated Database ALTER query
        query_2 = f"""
ALTER database [{database}] SET ANSI_NULL_DEFAULT OFF
ALTER database [{database}] SET ANSI_NULLS OFF 
ALTER database [{database}] SET ANSI_PADDING OFF 
ALTER database [{database}] SET ANSI_WARNINGS OFF 
ALTER database [{database}] SET ARITHABORT OFF 
ALTER database [{database}] SET AUTO_CLOSE OFF 
ALTER database [{database}] SET AUTO_SHRINK OFF 
ALTER database [{database}] SET AUTO_CREATE_STATISTICS ON(INCREMENTAL = OFF)
ALTER database [{database}] SET AUTO_UPDATE_STATISTICS ON 
ALTER database [{database}] SET CURSOR_CLOSE_ON_COMMIT OFF 
ALTER database [{database}] SET CURSOR_DEFAULT  GLOBAL 
ALTER database [{database}] SET CONCAT_NULL_YIELDS_NULL OFF 
ALTER database [{database}] SET NUMERIC_ROUNDABORT OFF 
ALTER database [{database}] SET QUOTED_IDENTIFIER OFF 
ALTER database [{database}] SET RECURSIVE_TRIGGERS OFF 
ALTER database [{database}] SET  DISABLE_BROKER 
ALTER database [{database}] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
ALTER database [{database}] SET DATE_CORRELATION_OPTIMIZATION OFF 
ALTER database [{database}] SET PARAMETERIZATION SIMPLE 
ALTER database [{database}] SET READ_COMMITTED_SNAPSHOT OFF 
ALTER database [{database}] SET  READ_WRITE 
ALTER database [{database}] SET RECOVERY SIMPLE 
ALTER database [{database}] SET  MULTI_USER 
ALTER database [{database}] SET PAGE_VERIFY CHECKSUM  
ALTER database [{database}] SET TARGET_RECOVERY_TIME = 0 SECONDS 
ALTER database [{database}] SET DELAYED_DURABILITY = DISABLED 
USE [{database}]
ALTER database SCOPED CONFIGURATION SET LEGACY_CARDINALITY_ESTIMATION = Off;
ALTER database SCOPED CONFIGURATION FOR SECONDARY SET LEGACY_CARDINALITY_ESTIMATION = Primary;
ALTER database SCOPED CONFIGURATION SET MAXDOP = 0;
ALTER database SCOPED CONFIGURATION FOR SECONDARY SET MAXDOP = PRIMARY;
ALTER database SCOPED CONFIGURATION SET PARAMETER_SNIFFING = On;
ALTER database SCOPED CONFIGURATION FOR SECONDARY SET PARAMETER_SNIFFING = Primary;
ALTER database SCOPED CONFIGURATION SET QUERY_OPTIMIZER_HOTFIXES = Off;
ALTER database SCOPED CONFIGURATION FOR SECONDARY SET QUERY_OPTIMIZER_HOTFIXES = Primary;
USE [{database}]
IF NOT EXISTS (SELECT name FROM sys.filegroups WHERE is_default=1 AND name = N'PRIMARY') ALTER database [{database}] MODIFY FILEGROUP [PRIMARY] DEFAULT
"""
        try:
            # Attempts to execute and commit the creation query
            cur.execute(query_1)
            con.commit()
            # Attempts to execute and commit the alter query
            cur.execute(query_2)
            con.commit()
        except Exception as err:
            print(f'Database Creation Failure:\n {err}\n\n')
            return err
        finally:
            # Closes the connection to the 'master' database
            cur.close()
            con.close()
        try:
            # Attempts to open the connection to the desired database
            con = connect_to_server(con_str_1)
            return con
        except:
            print(f'Database Connection Failure:\n {err}\n\n')
            return err

def query_builder_tables(file):
    """Builds query to build the required tables
    ACCEPTS: the file name that contains the primary query
    files are found in the 'Files\\SQL sub-directories
    The list comes from the 'QUERY_FILES_LIST' Constant parameter
    RETURNS: an assembled query including a prefixing 'USE' statement"""
    try:
        F_PATH = f'Files\\{file}.sql'
        with open(F_PATH) as open_file:
            query = f'USE [{database}]\n {open_file.read()}'
        return query
    except Exception as err:
        return err

def query_builder_insert(table='Contents'):
    """Structures a query to insert new values into a specified table
    ACCEPTS: the name of the table for which the query is being built
    RETURNS: the assembled query"""
    f_string = ', '.join(fields[table][0:])
    ##print(f_string)
    try:
        # builds the standard query string
        # INSERT INTO [TABLE] (Fields) VALUES (?s);
        query = f'USE [{database}]\n \
                    INSERT INTO [{table}] ({f_string}, updatedId)\n \
                    VALUES ('
        items = len(fields[table])
        i=0
        while i < items:
            i += 1
            query += '?, '
        query +='?);'
        return query
    except Exception as err:
        print(err)

def create_all_tables():
    """Creates and updates the main tables needed for primary data feed
    ACCEPTS: No Parameters
    RETURNS: nothing unless there is an error"""
    try:
        with connect_to_database() as con: # Creates and closes the Database Connection
            with con.cursor() as cur: # Creates and closes the cursor to work with the connected database
                # Creates all default tables and dependencies
                for file in QUERY_FILES_LIST:
                    query = query_builder_tables(file)
                    cur.execute(query)
                con.commit()
                # Populates the Categories with preliminary seed data
                # Currently Fails after introduction of updatedId (Uncertain Why)
                #query = f'USE [{database}]\n{BASE_DATA_ENTRY}'
                #cur.execute(query)
    except Exception as err:
        print(f'Potential error: \n{err}\n\n')

def generate_time_entry ():
    """creates guid and time entry for association to all table write/update processes
    ACCEPTS: No parameters
    RETURNS: current uuid for future tables"""
    uuid_current = str(uuid.uuid4())
    user_current = getuser()
    date_time_current = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
    values = [uuid_current, date_time_current, user_current]
    try:
        query = f'USE [{database}]\n \
                    INSERT INTO [Updated] (id, updatedAt, updatedByComputerUser)\n \
                    VALUES (?, ?, ?);'
        with connect_to_database() as con:
            with con.cursor() as cur:
                cur.execute(query, values)
                con.commit()
        return uuid_current
    except Exception as err:
        return err

def write_to_tables (uuid_current, table='Contents', stream=temp_values):
    """Enables the writing of CTC API Json streamed data to a table
    ACCEPTS: UUID for the current process, destination SQL table, and the data stream
    RETURNS: Success string or error"""
    with connect_to_database() as con:
        with con.cursor() as cur:
            query = query_builder_insert(table)
            values = []
            for item in stream['items']:
                # values = item.values()
                row = []
                for field in fields[table]:
                    if field == 'revitCategoryId':
                        try:
                            row.append(item['category']['id'])
                        except:
                            row.append(item['category'])
                    else:
                        if item[field] == False:
                            row.append(0)
                        elif item[field] == True:
                            row.append (1)
                        else:
                            row.append(item[field])
                row.append(uuid_current)
                values.append(tuple(row))
                # print(tuple(row))
                cur.execute(query, row)
                con.commit()
            try:
                # print(len(values[0][15]))
                values = tuple(values)
                cur.executemany(query, values)
                con.commit()
            except Exception as err:
                print(err)
    return f'completed table {table}'

def write_tables_sequential ():
    """Calls write_to_tables recursively to write the base tables in sequence
    ACCEPTS: nothing
    RETURNS: error if there is an issue in the flow"""
    # Creates a unique time entry for the current process
    uuid_current = generate_time_entry()
    for table in base_tables_list:
        try:
            write_to_tables(uuid_current, table, ctc.get_all_x(table, ctc.get_total_items(table)))
        except Exception as err:
            print(err)

def drop_database(database):
    """Rapidly drops the listed database for cleanup and testing"""
    query = f"""USE [master]
    ALTER database [{database}] set single_user with rollback immediate
    DROP database [{database}]
    """
    #print(query)
    try:
        with connect_to_server(CONN_STR_1) as con:
            with con.cursor() as cur:
                cur.execute(query)
                con.commit()
                print(f'\nSuccessfully removed database {database}\n')
    except Exception as err:
        return print(err)

''' DEPRECATED FUNCTION
# def write_ids (table='Contents', stream=temp_values, depth=''):
#     """Enables the writing of CTC API Json streamed data to a table"""
#     with connect_to_database() as con:
#         with con.cursor() as cur:
#             query = query_builder_insert(table)
#             #query = f'USE [{database}]\nINSERT INTO {table} (id)\nVALUES (?);'
#             values = []
#             for item in stream['items']:
#                 #values = item.values()
#                 row = []
#                 for field in fields[table]:
#                     if field == 'revitCategoryId':
#                         try:
#                             row.append(item['category']['id'])
#                         except:
#                             row.append(item['category'])
#                     else:
#                         if item[field] == False:
#                             row.append(0)
#                         elif item[field] == True:
#                             row.append (1)
#                         else:
#                             row.append(item[field])
#                 values.append(tuple(row))
#                 #print(tuple(row))
#                 cur.execute(query, row)
#                 con.commit()
#             try:
#                 #print(len(values[0][15]))
#                 values = tuple(values)
#                 cur.executemany(query, values)
#                 con.commit()
#             except Exception as err:
#                 print(err)
'''

''' DEPRECATED FUNCTION
# def write_tables_concurrent():
#     """Used to mutithread the writing of data to tables
#     Currently not working as expected"""
#     with cf.ProcessPoolExecutor() as executor:
#         if __name__ == '__main__':
#             for table in base_tables_list:
#                 results = executor.map(write_to_tables, table, ctc.get_all_x(table, ctc.get_total_items(table)))

#                 for result in results:
#                     print(result)
'''

# Testing Section for code
start_time = time.perf_counter()

# drop_database(db_name)
connect_to_database()
create_all_tables()
# write_tables_sequential()
#write_to_tables('Libraries', ctc.get_all_x('Libraries', ctc.get_total_items('Libraries')))

finish_time = time.perf_counter()
print(f'Finished in {round(finish_time-start_time, 2)} second(s)')
