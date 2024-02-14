''' primary entry point for the database connection '''
from Logging.ctc_logging import CTC_Log
from SQL_Connection.db_connection import get_db, engine
from SQL_Connection.Schemas.sch_all import core_schemas, create_schema
from SQL_Connection.Tables.tbl_core_refreshed import Tbl_Core_Refreshed
from SQL_Connection.Tables.tbl_cms_contents import Tbl_CMS_Contents

def main():
    for core_schema in core_schemas:
        create_schema(core_schema)
    # engine.connect() as connection:
    #     try:
    #         new_base = declarative_base()
    #         for core_schema in core_schemas:
    #             create_schema(core_schema)
    #             db.add(Tbl_Core_Refreshed)
    #             db.add(Tbl_CMS_Contents)
    #             db.commit()
    #     except Exception as err:
    #         CTC_Log("JSON").info(f'Schema: "{schema_name}" already exists')
    #         CTC_Log("JSON").error(str(err))
    #     finally:
    #         connection.close()