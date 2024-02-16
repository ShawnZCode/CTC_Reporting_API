''' primary entry point for the database connection '''
from Logging.ctc_logging import CTC_Log
from SQL_Connection.db_connection import get_db, engine, Base
from SQL_Connection.Schemas.sch_all import *
import SQL_Connection.Tables
from JSON.read_file import read_file

log_title = read_file("SQL_Connection\\Settings.json")['logTitle']

def create_all():
    for core_schema in core_schemas:
        create_schema(core_schema)
    Base.metadata.create_all(bind=engine)

## function to undo actions taken in the main function
def drop_all():
    CTC_Log(log_title).info('Begin dropping all tables and schemas')
    Base.metadata.drop_all(bind=engine)
    for core_schema in core_schemas:
        drop_schema(core_schema)
    CTC_Log(log_title).info('End dropping all tables and schemas')

create_all()