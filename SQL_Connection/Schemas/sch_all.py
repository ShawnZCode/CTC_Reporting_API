'''Module that generates all needed schemas for the database'''

## Import the needed libraries
from sqlalchemy import MetaData
from sqlalchemy.schema import CreateSchema
from SQL_Connection.db_connection import engine, get_db, session_local

## Create the 'core' schema for the database
core_schema_list = ['core', 'accounts', 'csl', 'cms', 'pal']
#metadata = MetaData()
#metadata.create_all(create_engine, checkfirst=True)
with engine.connect() as connection:
    try:
        for core_schema in core_schema_list:
            connection.execute(CreateSchema(core_schema, if_not_exists=True))
            connection.commit()
    finally:
        connection.close()

## Create the 'accounts' schema for the database


## Create the 'csl' schema for the database


## Create the 'cms' schema for the database


## Create the 'pal' schema for the database