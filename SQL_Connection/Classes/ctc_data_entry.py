"""This class is the core object which receives a JSON
    stream and converts it into SQL entries or pulls SQL
    entries for comparison with the incoming JSON stream."""
import json

from SQL_Connection.Classes.ctc_database_connection import CTCDatabaseObject
from SQL_Connection.Classes.ctc_query_object import CTCQueryObject

# import uuid
# from datetime import datetime
# from getpass import getuser


class CTCDataEntry:
    """This is the core object which takes in:
    TODO: Describe this function"""

    def __init__(self, connection: CTCDatabaseObject, query: CTCQueryObject):
        """Initialization method (constructor), establishing object values
        Expects 2 mandatory inputs:
        connection = as a CTCDatabaseObject active connection
        query = CTCQuery object"""

    def __enter__(self):
        """Context manager entry point"""
        return self

    def __exit__(self, type, value, traceback):
        """Context manager exit point"""
        self.__del__

    def __del__(self):
        """Self destruction to close out everything and clean up after the class"""
        output = str(self)
        try:
            del self
        finally:
            return f"{output} has been deleted"

    def __repr__(self):
        """Stock object representation method
        returns the core inputs of the object in quoted list"""
        return f'Data Object("{self.namespace}", "{self.table}", "{self.stream}")'

    def __str__(self):
        """string output"""
        return f"{self.connection}\nJSON Stream:\n{json.dumps(self.stream, indent=2)}"

    # def generate_time_entry (self):
    #     """creates guid and time entry for association to all table write/update processes
    #     ACCEPTS: No parameters
    #     RETURNS: assembled query string and current uuid for future tables"""
    #     uuid_current = str(uuid.uuid4())
    #     user_current = getuser()
    #     date_time_current = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
    #     #values = [uuid_current, date_time_current, user_current]
    #     try:
    #         query = self.query_insert
    #         return query, uuid_current
    #     except Exception as err:
    #         return err

    def __write_sql(self, table, sql_statement):
        """Writes main entry into SQL server
        Expects 2 mandatory inputs:
        table = Name of sql table as string
        sql statement = Full"""

        # TODO: Author the entirety of the write_sql method
        pass

    def __query_existing_sql(self):
        """Fetches all 'id', 'updatedAt' and 'refreshedAt' values"""
        # TODO: Author the entirety of the query_existing_sql method
        pass

    def __compare_for_updates(self):
        """Compares existing data values to the incoming JSON stream"""
        # TODO: Author the entirety of the compare_for_updates method
        pass

    def __update_sql(self, update_list, stream):
        """updated entries based on the comparison_for_updates method"""
        # TODO: Author the entirety of the update_sql method
        pass
