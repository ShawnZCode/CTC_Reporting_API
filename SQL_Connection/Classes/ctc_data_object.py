"""This class is the core object which receives a JSON
    stream and converts it into SQL entries or pulls SQL
    entries for comparison with the incoming JSON stream."""
import json
from JSON.Functions.read_file import read_file

class CTCDataObject():
    """This is the core object which takes in:
        SQL namespace,
        SQL Table Name
        JSON Data Stream"""

    def __init__(self, namespace, table, stream):
        """Initialization method (constructor), establishing object values
        Expects 3 mandatory inputs:
        namespace = api source from CTC's Web API and namespace in SQL
        table = the intended destination table for the dataset
        stream = JSON data stream from CTC's Web API"""
        self.namespace = namespace
        self.table = table
        self.stream = stream

    def __repr__(self):
        """Stock object representation method
        returns the core inputs of the object in quoted list"""
        return f'Data Object("{self.namespace}", "{self.table}", "{self.stream}")'

    def __str__(self):
        """string output"""
        return f'{self.namespace}.{self.table}:\n JSON Stream:\n{json.dumps(self.stream, indent=2)}'

    def write_sql(self, table, sql_statement):
        """Writes main entry into SQL server
        Expects 2 mandatory inputs:
        table = Name of sql table as string
        sql statement = Full """

        # TODO: Author the entirety of the write_sql method
        pass

    def query_existing_sql(self):
        """Fetches all 'id', 'updatedAt' and 'refreshedAt' values"""
        # TODO: Author the entirety of the query_existing_sql method
        pass

    def compare_for_updates(self):
        """Compares existing data values to the incoming JSON stream"""
        # TODO: Author the entirety of the compare_for_updates method
        pass

    def update_sql(self, update_list, stream):
        """updated entries based on the comparison_for_updates method"""
        # TODO: Author the entirety of the update_sql method
        pass
