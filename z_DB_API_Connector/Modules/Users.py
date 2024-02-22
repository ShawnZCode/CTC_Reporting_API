from sqlalchemy.orm import Session

from SQL_Connection.db_connection import NotFoundError, session_local
from SQL_Connection.tables.tbl_acc_users import (
    AccUser,
    AccUserRecord,
    AccUserRole,
    create_new_user,
    read_db_user,
    update_user,
)
from utils.read_file import read_file


def create_user(content: AccUser, db: Session) -> AccUser:
    db_content = create_new_user(item=content, session=db)
    return AccUser(**db_content.__dict__)


def create_update_users(items: dict):
    for content in items:
        full_item = AccUserRecord(**content, roles=content["roleAssignments"])
        item = AccUser(**full_item.model_dump())
        database = session_local()
        try:
            update_user(item=item, session=database)
            # create_roles(item, database)
        except NotFoundError:
            create_user(content=item, db=database)
        finally:
            database.close()
