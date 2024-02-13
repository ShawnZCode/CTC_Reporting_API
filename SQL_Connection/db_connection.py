"""Class used to create a database and return a database connection"""
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.ext.declarative import declarative_base

## Establish the async connection to the database for both postgres and mssql

class NotFoundError(Exception):
    pass

class Base(DeclarativeBase):
    pass
