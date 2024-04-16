"""Helper functions to generate the local cache files using the APICore Connection"""

# import time
import json
import os
from datetime import datetime
from multiprocessing import Pool, cpu_count

from APICore.main import (
    GET_DETAILS_FUNCTIONS_ALL,
    GET_DETAILS_FUNCTIONS_BY_ID,
    GET_FUNCTIONS,
)

# from Logging.ctc_logging import CTCLog
from utils.read_file import read_file

JSON_SETTINGS = read_file("JSON\\Settings.json")

CURRENT_DATE_TIME = datetime.now().strftime("%Y-%m-%d_%H-%M")

PROC_ALLOWED = int(round(cpu_count() / 2.5, 0))


def directory_create(
    *,
    root: str = JSON_SETTINGS["files"]["storageCachePath"],
    container: str = CURRENT_DATE_TIME,
) -> str:
    """Ensures a directory for cache of fetched files"""
    try:
        root_directory = f"{root}\\{container}"
        if not os.path.isdir(root_directory):
            os.makedirs(root_directory, exist_ok=True)
        return root_directory
    except Exception as err:
        raise err


def write_json_file(
    *,
    stream: dict,
    file_name: str,
    container: str = CURRENT_DATE_TIME,
    sub_directory: str = "CMS",
) -> None:
    """Writes a json file from streamed data"""
    try:
        file_path = f"{directory_create(container=container)}\\{sub_directory}"
        os.makedirs(file_path, exist_ok=True)
    except Exception as err:
        raise err
    try:
        file_path += f"\\{file_name}.json"
        with open(file=file_path, mode="w") as f:
            # f.write(json.dumps(stream, indent=4))
            json.dump(stream, f, indent=4)
            # CTCLog(LOG_TITLE).info(f"Saved {file_path}")
    except Exception as err:
        raise err
        # CTCLog(LOG_TITLE).error(str(err))


def get_base_json(file_name: str, function, date_time: str = CURRENT_DATE_TIME) -> None:
    records = function()
    records_json = json.loads(records.model_dump_json())
    write_json_file(
        stream=records_json,
        file_name=file_name.title(),
        container=date_time,
        sub_directory="Base",
    )


def get_all_jsons(date_time: str = CURRENT_DATE_TIME):
    bpool = Pool(processes=PROC_ALLOWED)
    for key, value in GET_FUNCTIONS.items():
        bpool.apply_async(
            func=get_base_json,
            args=(
                key,
                value,
                date_time,
            ),
        )
        if key in GET_DETAILS_FUNCTIONS_BY_ID.keys():
            dpool = Pool(processes=PROC_ALLOWED)
            objects = GET_FUNCTIONS[key]()
            for item in objects.items:
                dpool.apply_async(
                    func=get_detailed_json,
                    args=(key, GET_DETAILS_FUNCTIONS_BY_ID[key], item, date_time),
                )
            dpool.close()
            dpool.join()
    bpool.close()
    bpool.join()


def get_detailed_json(key: str, get_function, item, date_time: str = CURRENT_DATE_TIME):
    record = get_function(item=item)
    record_json = json.loads(record.model_dump_json())
    write_json_file(
        stream=record_json,
        file_name=f"{key.title()}_{record.id}",
        container=date_time,
        sub_directory=f"Details\\{key.title()}",
    )


if __name__ == "__main__":
    pass
