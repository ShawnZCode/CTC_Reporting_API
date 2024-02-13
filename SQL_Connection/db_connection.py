"""Class used to create a database and return a database connection"""
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from JSON.Functions.read_file import read_file

Base = declarative_base()
