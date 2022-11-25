"""General functions to connect with SQL server"""

import api_get_functions as ctc
from asyncio.windows_events import NULL
import pyodbc
import time
import json
import concurrent.futures as cf
from os import path
from json_cache_files import read_file, BASE_FILE_LIST

start_time = time.perf_counter()

settings = read_file('Files\\SupportFiles\\Settings.json')

driver=settings['sql']['driver']
server=settings['sql']['server']
api_key=settings['CTCAPI']['reportKey']
db_name = f'CTC Reporting {api_key}'
database=db_name
uid=settings['sql']['uid']
pwd=settings['sql']['pwd']

CONN_STR_1 = f'driver={driver};server={server};database={database};UID={uid};PWD={pwd};'
CONN_STR_2 = f'driver={driver};server={server};database=master;UID={uid};PWD={pwd};'

def connect_to_server(connect_string=None):
    """Initiates the server connection using credentials"""
    cs = connect_string ##or localhost_connect_string
    con = pyodbc.connect(cs, autocommit=True)
    return con

def connect_to_database(con_str_1=CONN_STR_1, con_str_2=CONN_STR_2):
    """Connects to the database or creates one if it doesn't exist"""
    try:
        con = connect_to_server(con_str_1)
        return con
    except Exception as err:
        #print(f'database Connection Failure:\n {err}\n\n')
        con = connect_to_server(con_str_2)
        cur = con.cursor()
        query_1 = f"""CREATE database [{database}]
    CONTAINMENT = NONE
    ON  PRIMARY 
( NAME = N'{database}', FILENAME = N'C:\Program Files\Microsoft SQL server\MSSQL14.MSSQLserver\MSSQL\DATA\{database}.mdf' , SIZE = 5120KB , FILEGROWTH = 10%)
    LOG ON 
( NAME = N'{database}_log', FILENAME = N'C:\Program Files\Microsoft SQL server\MSSQL14.MSSQLserver\MSSQL\DATA\{database}_log.ldf' , SIZE = 1024KB , FILEGROWTH = 10%)"""
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
        #print(query_1)
        #print(query_2)
        try:
            cur.execute(query_1)
            con.commit()
            cur.execute(query_2)
            con.commit()
            #return con
        except Exception as err:
            print(f'database Creation Failure:\n {err}\n\n')
            return err
        finally:
            cur.close()
            con.close()
        try:
            con = connect_to_server(con_str_1)
            return con
        except:
            print(f'database Connection Failure:\n {err}\n\n')
            return err

QUERY_FILES_LIST = ['SQL\\CMS\\Categories'
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
                ,'SQL\\CMS\\SavedSearchContentSources'
                ,'SQL\\CMS\\Saved-Searches'
                ,'SQL\\CMS\\SavedSearchLibraries'
                ,'SQL\\CMS\\SavedSearchPermissions'
                ,'SQL\\CMS\\SavedSearchRevitCategories'
                ,'SQL\\CMS\\SavedSearchTags'
                ,'SQL\\CMS\\SearchContentSources'
                ,'SQL\\CMS\\Searches'
                ,'SQL\\CMS\\SearchLibraries'
                ,'SQL\\CMS\\SearchResults'
                ,'SQL\\CMS\\SearchRevitCategories'
                ,'SQL\\CMS\\SearchTags'
                ,'SQL\\CMS\\Tags'
                ,'SQL\\CMS\\UserFavoriteContents'
                ,'SQL\\ORG\\Users']
                #,'SQL\\UPDATE_REFERENCES\\UpdateTables']
CSV = path.abspath('Files\\SupportFiles\\Categories.csv')
BASE_DATA_ENTRY = f"""BULK INSERT Categories
  FROM '{CSV}'
  WITH (FORMAT = 'CSV')"""
BASE_TABLES_LIST = BASE_FILE_LIST

def query_builder_tables(database, file):
    try:
        F_PATH = f'Files\\{file}.sql'
        with open(F_PATH) as open_file:
            query = f'USE [{database}]\n {open_file.read()}'
        return query
    except Exception as err:
        return err

def query_builder_insert(table='Contents'):
    """Structures a query to insert new values into a specified table"""
    f_string = ', '.join(fields[table][0:])
    ##print(f_string)
    try:
        query = f'USE [{database}]\n \
                    INSERT INTO [{table}] ({f_string})\n \
                    VALUES ('
        items = len(fields[table])
        i=0
        while i < items-1:
            i += 1
            query += '?, '
        query +='?);'
        return query
    except Exception as err:
        print(err)

def create_tables(conn1=CONN_STR_1, conn2=CONN_STR_2):
    """Creates the main tables needed for primary datafeed"""
    try:
        with connect_to_database(conn1, conn2) as con:
            with con.cursor() as cur:
                for file in QUERY_FILES_LIST:
                    query = query_builder_tables(db_name, file)
                    cur.execute(query)
                con.commit()
                query = f'USE [{database}]\n{BASE_DATA_ENTRY}'
                cur.execute(query)
    except Exception as err:
        print(f'Potential error: \n{err}\n\n')
        #print(query)

fields = read_file('Files\\SupportFiles\\Fields.json')
temp_values = read_file('Files\\z_StructureReference\\Contents5.json')

def write_to_tables (table='Contents', stream=temp_values, depth=''):
    """Enables the writing of CTC API Json streamed data to a table"""
    with connect_to_database() as con:
        with con.cursor() as cur:
            #cur.fast_executemany = True
            query = query_builder_insert(table)
            #query = f'USE [{database}]\nINSERT INTO {table} (id)\nVALUES (?);'
            values = []
            for item in stream['items']:
                #values = item.values()
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
                values.append(tuple(row))
                #print(tuple(row))
                cur.execute(query, row)
                con.commit()
            try:
                #print(len(values[0][15]))
                values = tuple(values)
                cur.executemany(query, values)
                con.commit()
            except Exception as err:
                print(err)
    return f'completed table {table}'

def write_ids (table='Contents', stream=temp_values, depth=''):
    """Enables the writing of CTC API Json streamed data to a table"""
    with connect_to_database() as con:
        with con.cursor() as cur:
            #cur.fast_executemany = True
            query = query_builder_insert(table)
            #query = f'USE [{database}]\nINSERT INTO {table} (id)\nVALUES (?);'
            values = []
            for item in stream['items']:
                #values = item.values()
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
                values.append(tuple(row))
                #print(tuple(row))
                cur.execute(query, row)
                con.commit()
            try:
                #print(len(values[0][15]))
                values = tuple(values)
                cur.executemany(query, values)
                con.commit()
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

def write_tables_concurrent():
    """Used to mutithread the writing of data to tables
    Currently not working as expected"""
    with cf.ProcessPoolExecutor() as executor:
        if __name__ == '__main__':
            for table in BASE_TABLES_LIST:
                results = executor.map(write_to_tables, table, ctc.get_all_x(table, ctc.get_total_items(table)))

                for result in results:
                    print(result)

def write_tables_sequential ():
    """Writes the base tables in sequence"""
    for table in BASE_TABLES_LIST:
        try:
            write_to_tables(table, ctc.get_all_x(table, ctc.get_total_items(table)))
        except Exception as err:
            print(err)

# drop_database(db_name)
connect_to_database()
create_tables()
write_tables_sequential()
#write_to_tables('Libraries', ctc.get_all_x('Libraries', ctc.get_total_items('Libraries')))

finish_time = time.perf_counter()
print(f'Finished in {round(finish_time-start_time, 2)} second(s)')
