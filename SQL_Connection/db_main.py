"""primary entry point for the database connection"""

import SQL_Connection.tables
from APICore.result_models.accounts.users_org import AccUser
from Logging.ctc_logging import CTCLog
from SQL_Connection.db_connection import Base, SessionLocal, engine, get_db
from SQL_Connection.schemas.sch_all import CORE_SCHEMAS, create_schema, drop_schema
from SQL_Connection.tables.accounts.tbl_acc_users import create_new_user
from SQL_Connection.tables.core.tbl_core_refreshed import create_new_refreshed
from utils.read_file import read_file

LOG_TITLE = read_file("SQL_Connection\\Settings.json")["logTitle"]


def create_all():
    for core_schema in CORE_SCHEMAS:
        create_schema(core_schema)
    Base.metadata.create_all(bind=engine)

    default_users = [
        AccUser(
            id="a2d03d2b-f3d5-43fe-b0bb-342c91c890c4",
            email="hive@ctcsoftware.com",
            displayName="HIVE Admin",
            department="Automation (do not change settings)",
            status="Active",
            addedById="a2d03d2b-f3d5-43fe-b0bb-342c91c890c4",
            updatedById="a2d03d2b-f3d5-43fe-b0bb-342c91c890c4",
            addedAt="2020-04-29T12:40:18.000Z",
            updatedAt="2024-04-17T14:53:14.642Z",
            isSSOUser=False,
        ),
        AccUser(
            id="d2989f9e-2443-4d6b-9260-83e3e93facba",
            email="shawnz@ctcsoftware.com",
            displayName="Shawn Zirbes",
            department="Automation (do not change settings)",
            status="Active",
            addedAt="2020-04-29T18:03:34.380Z",
            updatedAt="2024-04-25T15:10:30.250Z",
            addedById="a2d03d2b-f3d5-43fe-b0bb-342c91c890c4",
            updatedById="a2d03d2b-f3d5-43fe-b0bb-342c91c890c4",
            isSSOUser=False,
        ),
        AccUser(
            id="4b3b0318-ff9d-4fc5-a031-577f6b449446",
            email="chrisb@ctcsoftware.com",
            displayName="Chris Bercher",
            department="Automation (do not change settings)",
            status="Active",
            addedAt="2020-04-29T18:03:34.380Z",
            updatedAt="2024-04-25T15:10:30.250Z",
            addedById="a2d03d2b-f3d5-43fe-b0bb-342c91c890c4",
            updatedById="a2d03d2b-f3d5-43fe-b0bb-342c91c890c4",
            isSSOUser=False,
        ),
    ]
    refreshed = create_new_refreshed()
    [create_new_user(user, refreshed) for user in default_users]


## function to undo actions taken in the main function
def drop_all():
    CTCLog(LOG_TITLE).info("Begin dropping all tables and schemas")
    Base.metadata.drop_all(bind=engine)
    for core_schema in CORE_SCHEMAS:
        drop_schema(core_schema)
    CTCLog(LOG_TITLE).info("End dropping all tables and schemas")
