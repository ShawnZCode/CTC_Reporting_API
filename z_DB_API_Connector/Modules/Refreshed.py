from sqlalchemy.orm import Session

from SQL_Connection.db_connection import NotFoundError, session_local
from SQL_Connection.Tables.tbl_core_refreshed import (
    Refreshed,
    create_new_refreshed,
    get_last_refreshed,
)


def create_refreshed():
    database = session_local()
    try:
        refreshed: Refreshed = create_new_refreshed(session=database)
    finally:
        database.close()
    return refreshed


def fetch_last_refreshed():
    database = session_local()
    try:
        refreshed: Refreshed = get_last_refreshed(session=database)
    except NotFoundError:
        raise NotFoundError("No previous refresh records found")
    finally:
        database.close()
    return refreshed
