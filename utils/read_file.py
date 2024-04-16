"""Single Read File Function to save multiple definition."""

import json


def read_file(path):
    """Simple Function to open, read and close a file
    Returns the contents of a json file"""
    try:
        with open(path, "r") as open_file:
            contents = json.loads(open_file.read())
    except Exception as err:
        print(err)
        contents = {"": {"": {"": ""}}}
    return contents
