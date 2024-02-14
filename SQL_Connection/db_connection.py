"""Class used to create a database and return a database connection"""
import json
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import DeclarativeBase, sessionmaker, declarative_base

## Establish the async connection to the database for both postgres and mssql

class NotFoundError(Exception):
    pass

class Base(DeclarativeBase):
    pass

## MSSQL Connection settings
    ## Requires pyodbc to be installed
conn_url_mssql = URL.create(
    drivername= 'mssql+pyodbc',
    username= 'sa',
    password= 'T3$t!ngSA',
    host= 'CTCLTMNShawnZ',
#    port= '1433' 
    database= 'CTC_ReportingDB',
    query={"driver":"ODBC Driver 18 for SQL Server","TrustServerCertificate":"yes"}
)

## PostgreSQL COnnection Settings
    ## Requires psycopg2 to be installed
conn_url_postgresql = URL.create(
    drivername= 'postgresql+psycopg2',
    username= 'postgres',
    password= 'P0stgr3$',
    host= 'localhost',
    port= '5432',
    database= 'CTC_ReportingDB',
)

## Create the database engine and session
engine = create_engine(conn_url_postgresql)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the database session
def get_db():
    database = session_local()
    try:
        yield database
    finally:
        database.close()
