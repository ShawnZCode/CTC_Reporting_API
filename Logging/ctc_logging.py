"""Some basic logging functions to simplify logging
in all portions of the library collection"""

import logging
import os
from datetime import datetime

from utils.read_file import read_file

SETTINGS = read_file("Logging\\Settings.json")


class CTCLog:
    """Rebrand of 'logging' to facilitate consistent settings in all modules"""

    def __init__(self, library: str):
        """initialization"""
        root_directory = self.directory_create(library=library)
        self.current_date = datetime.now().strftime("%Y-%m-%d-%H-%M")
        self.library = library
        logging.basicConfig(
            filename=f"{root_directory}\\API_Log_{self.library}_{self.current_date}.log",
            level=logging.INFO,
            format="%(asctime)s,%(levelname)s,%(message)s",
        )

    def __del__(self, *args):
        del self

    def directory_create(self, library: str):
        """Ensures a directory for current date time cache of files"""
        try:
            logging_location = SETTINGS["loggingLocation"]
            root_directory = f"{logging_location}"
            if not os.path.isdir(root_directory):
                os.makedirs(name=root_directory, exist_ok=True)
                CTCLog(library=library).info(f"successfully made {root_directory}")
            return root_directory
        except Exception as err:
            CTCLog(library=library).error(str(err))

    def info(self, log_message: str):
        """Basic log function
        accepts the log message
        writes a log entry to the log file"""
        logging.info(log_message)

    def warning(self, log_message: str):
        """Basic log function
        accepts the log message
        writes a log entry to the log file"""
        logging.warning(log_message)

    def error(self, log_message: str):
        """Basic log function
        accepts the log message
        writes a log entry to the log file"""
        logging.error(log_message)

    def debug(self, log_message: str):
        """Basic log function
        accepts the log message
        writes a log entry to the log file"""
        logging.debug(log_message)
