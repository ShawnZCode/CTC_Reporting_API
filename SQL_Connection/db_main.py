"""primary entry point for the database connection"""

from APICore.main import GET_DETAILS_FUNCTIONS_BY_ID, GET_FUNCTIONS
from APICore.result_models.accounts.users_org import AccUser
from Logging.ctc_logging import CTCLog
from SQL_Connection import tables
from SQL_Connection.db_connection import Base, SessionLocal, engine, get_db
from SQL_Connection.schemas.sch_all import CORE_SCHEMAS, create_schema, drop_schema
from SQL_Connection.tables.accounts.tbl_acc_users import create_new_user
from SQL_Connection.tables.core.tbl_core_refreshed import create_new_refreshed
from utils.read_file import read_file

LOG_TITLE = read_file("SQL_Connection\\Settings.json")["logTitle"]

TABLE_WRITE_BASE = {
    "acc_roles": tables.create_new_role,
    "acc_users": tables.create_new_user,
    "acc_groups": tables.create_new_group,
    "csl_products": tables.create_new_product,
    "csl_licenses": tables.create_new_license,
    "cms_contents": tables.create_new_content,
    "cms_libraries": tables.create_new_library,
    "cms_tags": tables.create_new_tag,
    "cms_saved_searches": tables.create_new_saved_search,
    "cms_searches": tables.create_new_search,
    "pal_projects": tables.create_new_project,
    "pal_sessions": tables.create_new_session,
    "pal_doc_sessions": tables.create_new_doc_session,
}

TABLE_WRITE_DETAILS = {
    # "cms_contents",
    "cms_libraries",
    "cms_tags",
    # "cms_saved_searches",
    # "cms_searches",
    "csl_products",  # <- App Sessions
    "pal_projects",
    "pal_doc_sessions",
}


## function to create the database
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
            status="DEV",
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
            status="DEV",
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
            status="DEV",
            addedAt="2020-04-29T18:03:34.380Z",
            updatedAt="2024-04-25T15:10:30.250Z",
            addedById="a2d03d2b-f3d5-43fe-b0bb-342c91c890c4",
            updatedById="a2d03d2b-f3d5-43fe-b0bb-342c91c890c4",
            isSSOUser=False,
        ),
    ]
    refreshed = create_new_refreshed()
    [create_new_user(user, refreshed) for user in default_users]


## function to reset the database
def drop_all():
    CTCLog(LOG_TITLE).info("Begin dropping all tables and schemas")
    Base.metadata.drop_all(bind=engine)
    for core_schema in CORE_SCHEMAS:
        drop_schema(core_schema)
    CTCLog(LOG_TITLE).info("End dropping all tables and schemas")


def write_all_x(key, refreshed):
    """Write all data to the database"""
    collection_object = GET_FUNCTIONS[key]()
    for item in collection_object.items:
        if key in TABLE_WRITE_DETAILS:
            item = GET_DETAILS_FUNCTIONS_BY_ID[key](item=item)
        TABLE_WRITE_BASE[key](item, refreshed)


def write_all():
    """Write all data to the database"""
    new_refresh = tables.create_new_refreshed()
    for key in TABLE_WRITE_BASE.keys():
        write_all_x(key, new_refresh)
