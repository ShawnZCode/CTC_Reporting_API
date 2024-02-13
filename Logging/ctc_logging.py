"""Some basic logging functions to simplify logging
in all portions of the library collection"""

import logging
import os
from datetime import datetime

from JSON.read_file import read_file

settings = read_file("Logging\\Settings.json")


class CTC_Log:
    """Rebrand of 'logging' to facilitate consistent settings in all modules"""

    def __init__(self, library: str):
        """initialization"""
        root_directory = self.directory_create()
        self.current_date = datetime.now().strftime("%Y-%m-%d-%H-%M")
        self.library = library
        logging.basicConfig(
            filename=f"{root_directory}\\API_Log_{self.library}_{self.current_date}.log",
            level=logging.INFO,
            format="%(asctime)s,%(levelname)s,%(message)s",
        )

    def __del__(self, *args):
        del self

    def directory_create(self):
        """Ensures a directory for current date time cache of files"""
        try:
            setting = settings["loggingLocation"]
            root_directory = f"{setting}"
            if not os.path.isdir(root_directory):
                os.makedirs(root_directory, exist_ok=True)
                CTC_Log("JSON").info(f"successfully made {root_directory}")
            return root_directory
        except Exception as err:
            CTC_Log("JSON").error(str(err))

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
