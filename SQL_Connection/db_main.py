""" primary entry point for the database connection """
import SQL_Connection.Tables
from JSON.read_file import read_file
from Logging.ctc_logging import CTC_Log
from SQL_Connection.db_connection import Base, engine, get_db
from SQL_Connection.Schemas.sch_all import *

log_title = read_file("SQL_Connection\\Settings.json")["logTitle"]


def create_all():
    for core_schema in core_schemas:
        create_schema(core_schema)
    Base.metadata.create_all(bind=engine)


## function to undo actions taken in the main function
def drop_all():
    CTC_Log(log_title).info("Begin dropping all tables and schemas")
    Base.metadata.drop_all(bind=engine)
    for core_schema in core_schemas:
        drop_schema(core_schema)
    CTC_Log(log_title).info("End dropping all tables and schemas")
