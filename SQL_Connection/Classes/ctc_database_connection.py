"""Class used to create a database and return a database connection"""

import json

import pyodbc

from JSON.Functions.read_file import read_file


class CTCDatabaseObject:
    """This is the core object which takes in:"""

    api_settings = read_file("APICore_Connection\\Settings.json")
    sql_settings = read_file("SQL_Connection\\Settings.json")

    driver = sql_settings["connectionSettings"]["driver"]
    server = sql_settings["connectionSettings"]["server"]
    api_key = api_settings["CTCAPI"]["reportKey"]
    db_name = f"CTC Reporting {api_key}"
    uid = sql_settings["connectionSettings"]["uid"]
    pwd = sql_settings["connectionSettings"]["pwd"]

    connection = None

    def __init__(self):
        """Initialization method (constructor), establishes database object, schema, tables
        and relationships
        SETS database connection"""

        # Initial server connection
        try:
            with self.__database_connect("master") as temp_connection:
                # List databases
                database_list = self.__database_list(temp_connection)
                    # Create or connect to desired database
                if self.db_name not in database_list:
                    self.__database_create(temp_connection)
                    schemas = self.__schema_create()
                    self.__tables_create(schemas)
                    self.__tables_relationships_create()
            self.connection = self.__database_connect(self.db_name)
        except Exception as err:
            print(f"Connection Error: {err}")

    def __enter__(self):
        """Context manager entry point"""
        return self

    def __exit__(self, *args):
        """Context manager exit point"""
        self.__del__

    def __del__(self):
        """Self destruction to close out everything and clean up after the class"""
        output = str(self)
        try:
            self.connection.close()
            del self
        finally:
            return f"{output} has been deleted"

    def __repr__(self):
        """Stock object representation method
        returns the core inputs of the object in quoted list"""
        return f'Connection String:("{self.connection}")'

    def __str__(self):
        """string output"""
        return f'Settings:\n{json.dumps(self.sql_settings["connectionSettings"], indent=2)}'

    def __database_list(self, connection):
        """RETURNS a list of databases
        Used to determine if a database needs to be created or can be deleted"""
        query = "SELECT name FROM sys.databases"
        try:
            with connection.cursor() as cursor:
                table = cursor.execute(query)
                tables = cursor.fetchall()
                table_list = []
                for table in tables:
                    table_list.append(table[0])
                return table_list
        except:
            return "no valid connection available"

    def __database_connect(self, database):
        """Connection to database
        EXPECTS: database name
        SETS: self.connection"""
        try:
            db_name = database
            conn_str = f"driver={self.driver};server={self.server};database={db_name};UID={self.uid};PWD={self.pwd};"
            connection = pyodbc.connect(conn_str, autocommit=True)
            return connection
        except Exception as err:
            print(f"Database Connection Error: {err}")
            return err

    def __database_create(self, connection=connection):
        """Creates preliminary empty database
        All default settings come from APICore_Connection\\Settings.json"""
        # TODO: Author the entirety of the database_create method
        with connection.cursor() as cursor_create:
            query_1 = f"""CREATE database [{self.db_name}]
        CONTAINMENT = NONE
        ON  PRIMARY 
    ( NAME = N'{self.db_name}', FILENAME = N'C:\Program Files\Microsoft SQL server\MSSQL14.MSSQLserver\MSSQL\DATA\{self.db_name}.mdf' , SIZE = 5120KB , FILEGROWTH = 10%)
        LOG ON 
    ( NAME = N'{self.db_name}_log', FILENAME = N'C:\Program Files\Microsoft SQL server\MSSQL14.MSSQLserver\MSSQL\DATA\{self.db_name}_log.ldf' , SIZE = 1024KB , FILEGROWTH = 10%)"""
            # vvv Dedicated Database ALTER query
            query_2 = f"""
    ALTER database [{self.db_name}] SET ANSI_NULL_DEFAULT OFF
    ALTER database [{self.db_name}] SET ANSI_NULLS OFF 
    ALTER database [{self.db_name}] SET ANSI_PADDING OFF 
    ALTER database [{self.db_name}] SET ANSI_WARNINGS OFF 
    ALTER database [{self.db_name}] SET ARITHABORT OFF 
    ALTER database [{self.db_name}] SET AUTO_CLOSE OFF 
    ALTER database [{self.db_name}] SET AUTO_SHRINK OFF 
    ALTER database [{self.db_name}] SET AUTO_CREATE_STATISTICS ON(INCREMENTAL = OFF)
    ALTER database [{self.db_name}] SET AUTO_UPDATE_STATISTICS ON 
    ALTER database [{self.db_name}] SET CURSOR_CLOSE_ON_COMMIT OFF 
    ALTER database [{self.db_name}] SET CURSOR_DEFAULT  GLOBAL 
    ALTER database [{self.db_name}] SET CONCAT_NULL_YIELDS_NULL OFF 
    ALTER database [{self.db_name}] SET NUMERIC_ROUNDABORT OFF 
    ALTER database [{self.db_name}] SET QUOTED_IDENTIFIER OFF 
    ALTER database [{self.db_name}] SET RECURSIVE_TRIGGERS OFF 
    ALTER database [{self.db_name}] SET  DISABLE_BROKER 
    ALTER database [{self.db_name}] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
    ALTER database [{self.db_name}] SET DATE_CORRELATION_OPTIMIZATION OFF 
    ALTER database [{self.db_name}] SET PARAMETERIZATION SIMPLE 
    ALTER database [{self.db_name}] SET READ_COMMITTED_SNAPSHOT OFF 
    ALTER database [{self.db_name}] SET  READ_WRITE 
    ALTER database [{self.db_name}] SET RECOVERY SIMPLE 
    ALTER database [{self.db_name}] SET  MULTI_USER 
    ALTER database [{self.db_name}] SET PAGE_VERIFY CHECKSUM  
    ALTER database [{self.db_name}] SET TARGET_RECOVERY_TIME = 0 SECONDS 
    ALTER database [{self.db_name}] SET DELAYED_DURABILITY = DISABLED 
    USE [{self.db_name}]
    ALTER database SCOPED CONFIGURATION SET LEGACY_CARDINALITY_ESTIMATION = Off;
    ALTER database SCOPED CONFIGURATION FOR SECONDARY SET LEGACY_CARDINALITY_ESTIMATION = Primary;
    ALTER database SCOPED CONFIGURATION SET MAXDOP = 0;
    ALTER database SCOPED CONFIGURATION FOR SECONDARY SET MAXDOP = PRIMARY;
    ALTER database SCOPED CONFIGURATION SET PARAMETER_SNIFFING = On;
    ALTER database SCOPED CONFIGURATION FOR SECONDARY SET PARAMETER_SNIFFING = Primary;
    ALTER database SCOPED CONFIGURATION SET QUERY_OPTIMIZER_HOTFIXES = Off;
    ALTER database SCOPED CONFIGURATION FOR SECONDARY SET QUERY_OPTIMIZER_HOTFIXES = Primary;
    USE [{self.db_name}]
    IF NOT EXISTS (SELECT name FROM sys.filegroups WHERE is_default=1 AND name = N'PRIMARY') ALTER database [{self.db_name}] MODIFY FILEGROUP [PRIMARY] DEFAULT
    """
            try:
                # Attempts to execute and commit the creation query
                cursor_create.execute(query_1)
                connection.commit()
                # Attempts to execute and commit the alter query
                cursor_create.execute(query_2)
                connection.commit()
                self.connection = self.__database_connect(self.db_name)
            except Exception as err:
                print(f"Database Creation Failure:\n {err}\n\n")
                return err

    def database_delete(self):
        """Deletes the listed database"""
        # TODO: Author the entirety of the database_delete method
        query = f"""USE [master]
    ALTER database [{self.db_name}] set single_user with rollback immediate
    DROP database [{self.db_name}]
    """
        # print(query)
        try:
            with self.connection.cursor() as cursor_delete:
                cursor_delete.execute(query)
                self.connection.commit()
                print(f"\nSuccessfully removed database {self.db_name}\n")
        except Exception as err:
            return print(err)

    def __schema_create(self):
        """Creates the scope listings needed by tables create
        RETURNS list of schemas to facilitate table creation by schema"""
        schemas_list = self.sql_settings["databaseSettings"].keys()
        for schema in schemas_list:
            query_1 = f"USE [{self.db_name}]"
            query_2 = f"CREATE SCHEMA [{schema}]"
            try:
                with self.connection.cursor() as cursor:
                    cursor.execute(query_1)
                    self.connection.commit()
                    cursor.execute(query_2)
                self.connection.commit()
            except Exception as err:
                return err
        return schemas_list

    def __tables_create_query(self, file):
        """Builds query to build the required tables
        ACCEPTS: the file name that contains the primary query
        files are found in the 'Files\\SQL sub-directories
        The list comes from the 'QUERY_FILES_LIST' Constant parameter
        RETURNS: an assembled query including a prefixing 'USE' statement"""
        try:
            F_PATH = f"{file}.sql"
            with open(F_PATH) as open_file:
                query = f"USE [{self.db_name}]\n {open_file.read()}"
            return query
        except Exception as err:
            return err

    def __tables_create(self, schemas):
        """Generates all tables listed in the SQL_Settings.json file"""
        connection = self.connection
        settings = self.sql_settings
        try:
            with connection.cursor() as cursor:
                for schema in schemas:
                    tables = settings['databaseSettings'][schema].keys()
                    for table in tables:
                        sql_file = settings['databaseSettings'][schema][table]['sqlTableQuery']
                        if sql_file is None:
                            continue
                        file = f'SQL_Connection\\References\\SQL\\{schema}\\{sql_file}'
                        query = self.__tables_create_query(file)
                        cursor.execute(query)
                        connection.commit()
        except Exception as err:
            print(f'Potential error: \n{err}\n\n')

    def tables_list(self):
        """Simple method intended to list all tables in the database"""
        # TODO: Author the entirety of the tables_list method
        query = "SELECT * FROM information_schema.tables;"
        try:
            with self.connection.cursor() as cursor:
                result = cursor.execute(query)
            self.connection.commit()
            return result
        except Exception as err:
            return err

    def __tables_relationships_create(self):
        """Creates all needed (Hardcoded) table relationships"""
        # TODO: Author the entirety of the create_relationships method
        pass

    def __tables_relationships_delete(self):
        """Removes all table relationships"""
