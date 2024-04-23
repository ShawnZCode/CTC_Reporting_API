"""Module that generates all needed schemas for the database"""

## Import the needed libraries
from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base
from sqlalchemy.schema import CreateSchema, DropSchema
from sqlalchemy.schema import MetaData as MD

from Logging.ctc_logging import CTCLog
from SQL_Connection.db_connection import engine, get_db
from utils.read_file import read_file

LOG_TITLE = read_file("SQL_Connection\\Settings.json")["logTitle"]
## List of schemas for the database
CORE_SCHEMAS = ["core", "accounts", "csl", "cms", "pal"]


## Create Schema Function
def create_schema(schema_name):
    with engine.connect() as connection:
        try:
            new_base = declarative_base()
            reflect = new_base.metadata.reflect(schema=schema_name, bind=connection)
            if reflect == None:
                connection.execute(CreateSchema(schema_name, if_not_exists=False))
                connection.commit()
                CTCLog(LOG_TITLE).info(f'Schema: "{schema_name}" successfully created')
            else:
                pass
        except Exception as err:
            CTCLog(LOG_TITLE).info(f'Schema: "{schema_name}" already exists')
            CTCLog(LOG_TITLE).error(str(err))
        finally:
            connection.close()


## Delete Schema Function
def drop_schema(schema_name):
    with engine.connect() as connection:
        try:
            connection.execute(DropSchema(schema_name, if_exists=True))
            connection.commit()
            CTCLog(LOG_TITLE).info(f'Schema: "{schema_name}" successfully deleted')
        except Exception as err:
            CTCLog(LOG_TITLE).info(f'Schema: "{schema_name}" does not exist')
            CTCLog(LOG_TITLE).error(str(err))
        finally:
            connection.close()


if __name__ == "__main__":
    for core_schema in CORE_SCHEMAS:
        create_schema(core_schema)
