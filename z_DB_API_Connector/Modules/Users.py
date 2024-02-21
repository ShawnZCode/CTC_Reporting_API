from sqlalchemy.orm import Session

from JSON.read_file import read_file
from SQL_Connection.db_connection import NotFoundError, session_local
from SQL_Connection.Tables.tbl_acc_users import (
    Acc_User,
    Acc_UserRecord,
    Acc_UserRoles,
    create_new_user,
    read_db_user,
    update_user,
)


def create_user(content: Acc_User, db: Session) -> Acc_User:
    db_content = create_new_user(item=content, session=db)
    return Acc_User(**db_content.__dict__)


def create_update_users(items: dict):
    for content in items:
        full_item = Acc_UserRecord(**content, roles=content["roleAssignments"])
        item = Acc_User(**full_item.model_dump())
        database = session_local()
        try:
            update_user(item=item, session=database)
            # create_roles(item, database)
        except NotFoundError:
            create_user(content=item, db=database)
        finally:
            database.close()
