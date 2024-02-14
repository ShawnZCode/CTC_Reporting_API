'''Module that generates all needed schemas for the database'''

## Import the needed libraries
from sqlalchemy import MetaData
from sqlalchemy.schema import CreateSchema, MetaData as MD
from sqlalchemy.orm import declarative_base
from SQL_Connection.db_connection import engine, get_db, session_local
from Logging.ctc_logging import CTC_Log

## Create the 'core' schema for the database
core_schemas = ['core', 'accounts', 'csl', 'cms', 'pal']

## Create Schema Function
def create_schema(schema_name):
    
    with engine.connect() as connection:
        try:
            new_base = declarative_base()
            reflect = new_base.metadata.reflect(schema=schema_name, bind=connection)
            if reflect == None:
                connection.execute(CreateSchema(schema_name, if_not_exists=False))
                connection.commit()
                CTC_Log("JSON").info(f'Schema: "{schema_name}" cuccessfully created')
            else:
                pass
        except Exception as err:
            CTC_Log("JSON").info(f'Schema: "{schema_name}" already exists')
            CTC_Log("JSON").error(str(err))
        finally:
            connection.close()

if __name__ == '__main__':
    for core_schema in core_schemas:
        create_schema(core_schema)
