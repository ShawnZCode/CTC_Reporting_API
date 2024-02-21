"""Class used to create a database and return a database connection"""
from sqlalchemy import URL, create_engine
from sqlalchemy.orm import DeclarativeBase, declarative_base, sessionmaker

from JSON.read_file import read_file

## Define the connection settings for the database
settings = read_file("SQL_Connection\\Settings.json")
match settings["serverLanguage"]:
    case "mssql":
        settings = settings["mssqlConnectionSettings"]
    case "postgresql":
        settings = settings["postresqlConnectionSettings"]

## SQL Connection settings
## Requires pyodbc to be pip installed when using mssql
## Requires psycopg2 to be pip installed when using postgresql
conn_url = URL.create(
    drivername=settings["driver"],
    username=settings["uid"],
    password=settings["pwd"],
    host=settings["host"],
    port=settings["port"],
    database=settings["db"],
    query=settings["query"],
)


class NotFoundError(Exception):
    pass


class Base(DeclarativeBase):
    pass


## Create the database engine and session
engine = create_engine(conn_url)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


# Dependency to get the database session
def get_db():
    database = session_local()
    try:
        yield database
    finally:
        database.close()
