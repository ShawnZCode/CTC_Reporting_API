"""This class is the core data object which receives a JSON
    stream and prepares it for SQL entries or receives SQL
    entries for comparison with the incoming JSON stream."""
from dataclasses import dataclass


@dataclass
class CTCDataObject:
    """dataobject used to manage the json stream or sql query"""
