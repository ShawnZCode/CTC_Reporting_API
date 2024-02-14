''' primary entry point for the database connection '''
from Logging.ctc_logging import CTC_Log
from SQL_Connection.db_connection import get_db, engine, Base
from SQL_Connection.Schemas.sch_all import core_schemas, create_schema
from SQL_Connection.Tables.tbl_acc_users import Tbl_Acc_Users
from SQL_Connection.Tables.tbl_acc_groups import Tbl_Acc_Groups
from SQL_Connection.Tables.tbl_core_refreshed import Tbl_Core_Refreshed
from SQL_Connection.Tables.tbl_cms_contents import Tbl_CMS_Contents

def main():
    for core_schema in core_schemas:
        create_schema(core_schema)
    Base.metadata.create_all(bind=engine)


main()