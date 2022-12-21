"""Routines to generate the local cache files from the CTC API"""

# import time
import json
import os
from datetime import datetime

from tqdm import tqdm

from APICore_Connection.Functions import api_get_functions as ctc
from JSON.Functions.read_file import read_file
from Logging.Functions.ctc_logging import CTC_Log

BASE_FILE_LIST = ["Contents", "Libraries", "Saved-Searches", "Searches", "Tags"]

api_settings = read_file("APICore_Connection\\Settings.json")
json_settings = read_file("JSON\\Settings.json")
api_settings_scopes = api_settings["scopes"]

current_date_time = datetime.now().strftime("%Y-%m-%d_%H-%M")


def directory_create(current_date_time):
    """Ensures a directory for current date time cache of files"""
    try:
        setting = json_settings["files"]["storageCachePath"]
        root_directory = f"{setting}\\{current_date_time}"
        if not os.path.isdir(root_directory):
            os.makedirs(root_directory, exist_ok=True)
            CTC_Log("JSON").info(f"successfully made {root_directory}")
        return root_directory
    except Exception as err:
        CTC_Log("JSON").error(str(err))


def write_json_file(stream, file_name, sub_directory="CMS"):
    """Writes a json file from streamed data"""
    try:
        file_path = f"{directory_create(current_date_time)}\\{sub_directory}"
        os.makedirs(file_path, exist_ok=True)
    except:
        pass
    try:
        file_path += f"\\{file_name}.json"
        with open(file_path, "w") as f:
            # f.write(json.dumps(stream, indent=4))
            json.dump(stream, f, indent=4)
            CTC_Log("JSON").info(f"Saved {file_path}")
    except Exception as err:
        CTC_Log("JSON").error(str(err))


def get_base_jsons():
    """Writes the original Json Files"""
    try:
        scopes_pbar = tqdm(
            api_settings_scopes, desc="Fetching base scopes: ", ncols=140
        )
        for scope in scopes_pbar:
            scopes_pbar.set_description(f"Fetching base collections from {scope}: ")
            collections_pbar = tqdm(
                api_settings_scopes[scope],
                desc=f"Base collections: ",
                ncols=140,
            )
            for collection in collections_pbar:
                collections_pbar.set_description(
                    f"Fetching base details for {collection} in {scope}"
                )
                count = api_settings_scopes[scope][collection]["mandatorySwitches"]
                if len(count) == 0:
                    collection_total = ctc.get_total_items(scope, collection)
                    collection_stream = ctc.get_all_x(
                        scope, collection, collection_total
                    )
                    write_json_file(collection_stream, collection, scope)
                collections_pbar.set_description(
                    f"Fetched base details for {collection} in {scope}"
                )
            scopes_pbar.set_description(f"Fetched base collections from {scope}: ")
    except Exception as err:
        CTC_Log("JSON").error(str(err))
    try:
        get_nested_jsons()
    except Exception as err:
        CTC_Log("JSON").error(str(err))


def get_ids(scope: str, collection: str):
    """Parses the saved Json file from parents and returns a list of ids
    ids are used to fetch the child detailed item from the api"""
    try:
        file_path = f"{directory_create(current_date_time)}\\{scope}"
        file_path += f"\\{collection}.json"
        with open(file_path, "r") as f:
            stream = json.loads(f.read())
    except Exception as err:
        CTC_Log("JSON").error(str(err))
    try:
        ids = []
        for i in stream["items"]:
            ids.append(i["id"])
        return ids
    except Exception as err:
        CTC_Log("JSON").error(str(err))


def get_nested_jsons():
    """Writes the nested Json files by id"""
    try:
        for scope in api_settings_scopes:
            collections_pbar = tqdm(
                api_settings_scopes[scope], desc="Collections: ", ncols=140
            )
            for collection in collections_pbar:
                collections_pbar.set_description(
                    f"{collection} item details in {scope}: "
                )
                if len(api_settings_scopes[scope][collection]["mandatorySwitches"]) > 0:
                    # fetches a list of ids from main dump
                    ids = get_ids(
                        scope, api_settings_scopes[scope][collection]["parent"]
                    )
                    ids_pbar = tqdm(ids, desc="Item Details: ", ncols=160)
                    for xId in ids_pbar:
                        ids_pbar.set_description(
                            f"Currently fetching {xId.lower()} from {scope}.{collection}: "
                        )
                        file_name = f"{collection}_{xId}"
                        item_stream = ctc.get_x_by_id(scope, collection, xId)
                        write_json_file(
                            item_stream, file_name, f"{scope}\\{collection}"
                        )
                        ids_pbar.set_description(
                            f"Currently fetched {len(ids)} ids from {scope}.{collection}: "
                        )

    except Exception as err:
        CTC_Log("JSON").error(str(err))
