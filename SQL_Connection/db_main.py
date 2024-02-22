""" primary entry point for the database connection """
import SQL_Connection.tables
from Logging.ctc_logging import CTCLog
from SQL_Connection.db_connection import Base, engine, get_db
from SQL_Connection.schemas.sch_all import CORE_SCHEMAS, create_schema, drop_schema
from utils.read_file import read_file

LOG_TITLE = read_file("SQL_Connection\\Settings.json")["logTitle"]


def create_all():
    for core_schema in CORE_SCHEMAS:
        create_schema(core_schema)
    Base.metadata.create_all(bind=engine)


## function to undo actions taken in the main function
def drop_all():
    CTCLog(LOG_TITLE).info("Begin dropping all tables and schemas")
    Base.metadata.drop_all(bind=engine)
    for core_schema in CORE_SCHEMAS:
        drop_schema(core_schema)
    CTCLog(LOG_TITLE).info("End dropping all tables and schemas")
