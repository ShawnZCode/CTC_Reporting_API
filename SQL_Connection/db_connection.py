"""Class used to create a database and return a database connection"""

from sqlalchemy import URL, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, declarative_base, sessionmaker

from utils.read_file import read_file

## Define the connection settings for the database
SETTINGS_IMPORT = read_file("SQL_Connection\\Settings.json")
match SETTINGS_IMPORT["serverLanguage"]:
    case "mssql":
        SETTINGS = SETTINGS_IMPORT["mssqlConnectionSettings"]
    case "postgresql":
        SETTINGS = SETTINGS_IMPORT["postresqlConnectionSettings"]

## SQL Connection settings
## Requires pyodbc to be pip installed when using mssql
## Requires psycopg2 to be pip installed when using postgresql
conn_url = URL.create(
    drivername=SETTINGS["driver"],
    username=SETTINGS["uid"],
    password=SETTINGS["pwd"],
    host=SETTINGS["host"],
    port=SETTINGS["port"],
    database=SETTINGS["db"],
    query=SETTINGS["query"],
)


class NotFoundError(Exception):
    pass


class Base(DeclarativeBase):
    pass


## Create the database engine and session
engine = create_engine(conn_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


# Dependency to get the database session
def get_db():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()
