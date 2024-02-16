'''Module that generates all needed schemas for the database'''

## Import the needed libraries
from sqlalchemy import MetaData
from sqlalchemy.schema import CreateSchema, DropSchema, MetaData as MD
from sqlalchemy.orm import declarative_base
from SQL_Connection.db_connection import engine, get_db, session_local
from Logging.ctc_logging import CTC_Log
from JSON.read_file import read_file

log_title = read_file("SQL_Connection\\Settings.json")['logTitle']

## Create Schema Function
def create_schema(schema_name):
    
    with engine.connect() as connection:
        try:
            new_base = declarative_base()
            reflect = new_base.metadata.reflect(schema=schema_name, bind=connection)
            if reflect == None:
                connection.execute(CreateSchema(schema_name, if_not_exists=False))
                connection.commit()
                CTC_Log(log_title).info(f'Schema: "{schema_name}" successfully created')
            else:
                pass
        except Exception as err:
            CTC_Log(log_title).info(f'Schema: "{schema_name}" already exists')
            CTC_Log(log_title).error(str(err))
        finally:
            connection.close()

## Delete Schema Function
def drop_schema(schema_name):
    with engine.connect() as connection:
        try:
            connection.execute(DropSchema(schema_name, if_exists=True))
            connection.commit()
            CTC_Log(log_title).info(f'Schema: "{schema_name}" successfully deleted')
        except Exception as err:
            CTC_Log(log_title).info(f'Schema: "{schema_name}" does not exist')
            CTC_Log(log_title).error(str(err))
        finally:
            connection.close()

## List of schemas for the database
core_schemas = ['core', 'accounts', 'csl', 'cms', 'pal']

if __name__ == '__main__':
    for core_schema in core_schemas:
        create_schema(core_schema)
