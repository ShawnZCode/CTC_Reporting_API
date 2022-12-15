"""This class is the core object which receives a JSON
    stream and converts it into SQL entries or pulls SQL
    entries for comparison with the incoming JSON stream."""
import json
import uuid
from datetime import datetime
from getpass import getuser

from JSON.Functions.read_file import read_file


class CTCDataEntry():
    """This is the core object which takes in:
        SQL Scope,
        SQL Table Name
        JSON Data Stream"""
    sql_settings = read_file('SQL_Connection\\Settings.json')
    sql_settings_scopes = sql_settings['databaseSettings']

    def __init__(self, database_name: str, scope: str, table_settings: dict, stream: json=None):
        """Initialization method (constructor), establishing object values
        Expects 3 mandatory inputs:
        scope = api source from CTC's Web API and scope in SQL
        table = single table key and all settings for that table
        stream = JSON data stream from CTC's Web API"""
        self.database_name = database_name
        self.scope = scope
        self.table_settings = table_settings
        self.stream = stream

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
        return f'{self.scope}.{self.table_name}:\n JSON Stream:\n{json.dumps(self.stream, indent=2)}'

    @property
    def table_name(self):
        """Generates the table name from the table_settings"""
        return self.table_settings['sqlTableQuery']

    @property
    def table_columns(self):
        """Generates a list of table columns from table_settings"""
        return list(self.table_settings['keysMap'].keys())

    @property
    def query_select (self,
            optional_where:str=None):
        """Selection Query Builder
        ACCEPTS:
                database as string
                tablename as string
        RETURNS: selection query as string"""
        column_string = ', '.join(self.table_columns[0:])
        # Assemble the full query
        query = f'USE [{self.database_name}];\n \
                SELECT {column_string}\n \
                FROM [{self.scope}].[{self.table_name}]'
        if optional_where is not None:
            query += f'\nWHERE {optional_where}'
        return query

    @property
    def query_insert(self):
        """Structures a query string to insert new values into a specified table
        ACCEPTS: the name of the table for which the query is being built
        RETURNS: the assembled query"""
        column_string = ', '.join(self.table_columns[0:])
        questions = []
        for _ in self.table_columns:
            questions.append('?')
        question_string = ', '.join(questions[0:])
        ##print(f_string)
        try:
            # builds the standard query string
            # INSERT INTO [TABLE] (Fields) VALUES (?s);
            query = f'USE [{self.database_name}]\n \
                        INSERT INTO [{self.scope}].[{self.table_name}] ({column_string})\n \
                        VALUES ({question_string});'
            return query
        except Exception as err:
            print(err)

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
        sql statement = Full """

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
