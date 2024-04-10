"""Helper functions to generate the local cache files using the APICore Connection"""

# import time
import json
import os
from datetime import datetime

# from pydantic import BaseModel
from tqdm.auto import tqdm

from APICore import api_get_functions as ctc
from APICore.connection_models.base import Collection, Scope
from APICore.connection_models.scopes import API_SCOPES
from Logging.ctc_logging import CTCLog
from utils.read_file import read_file

# BASE_FILE_LIST = ["Contents", "Libraries", "Saved-Searches", "Searches", "Tags"]

API_SETTINGS = read_file("APICore_Connection\\Settings.json")
API_SETTINGS_SCOPES = API_SETTINGS["scopes"]
JSON_SETTINGS = read_file("JSON\\Settings.json")
LOG_TITLE = JSON_SETTINGS["logTitle"]

CURRENT_DATE_TIME = datetime.now().strftime("%Y-%m-%d_%H-%M")


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
        CTCLog(LOG_TITLE).error(str(err))


def get_base_jsons(*, container: str = CURRENT_DATE_TIME) -> None:
    """Writes the original Json Files"""
    try:
        with tqdm(
            API_SETTINGS_SCOPES, desc="Fetching base scopes", ncols=130
        ) as scopes_pbar:
            for scope in scopes_pbar:
                scopes_pbar.set_description(f"Fetching base collections from {scope}")
                with tqdm(
                    API_SETTINGS_SCOPES[scope], desc="Base collections", ncols=130
                ) as collections_pbar:
                    for collection in collections_pbar:
                        collections_pbar.set_description(
                            f"Fetching base details for {collection} in {scope}"
                        )
                        count = API_SETTINGS_SCOPES[scope][collection][
                            "mandatorySwitches"
                        ]
                        if len(count) == 0:
                            collection_total = ctc.get_total_items(
                                scope=scope, collection=collection
                            )
                            collection_stream = ctc.get_all_x(
                                scope=scope,
                                collection=collection,
                                total_rows=collection_total,
                            )
                            write_json_file(
                                stream=collection_stream,
                                file_name=collection,
                                container=container,
                                sub_directory=scope,
                            )
                        collections_pbar.set_description(
                            f"Fetched base details for {collection} in {scope}"
                        )
                scopes_pbar.set_description(f"Fetched base collections from {scope}")
    except Exception as err:
        CTCLog(LOG_TITLE).error(str(err))
    finally:
        CTCLog(LOG_TITLE).info("Finished fetching base collections")
        tqdm._instances.clear()


def get_ids(
    *,
    scope: Scope,
    collection: Collection,
    container: str = CURRENT_DATE_TIME,
) -> list:
    """Parses the saved Json file from parents and returns a list of ids
    ids are used to fetch the child detailed item from the api"""
    try:
        file_path = f"{directory_create(container=container)}\\{scope.name}"
        file_path += f"\\{collection}.json"
        with open(file_path, "r") as f:
            stream = json.loads(f.read())
    except Exception as err:
        CTCLog(LOG_TITLE).error(str(err))
    try:
        ids = []
        for i in stream["items"]:
            if collection != "search":
                ids.append(i["id"])
            else:
                ids.append(i["searchId"])
        return ids
    except Exception as err:
        CTCLog(LOG_TITLE).error(str(err))


def get_xs_nested_jsons(scope: dict = {"scope": "cms"}) -> None:
    pass


def get_nested_jsons(
    scopes: list[dict] = API_SETTINGS_SCOPES,
    container: str = CURRENT_DATE_TIME,
    collection_override: str = None,
) -> None:
    """Fetches and writes the nested Json files by id"""
    try:
        for scope in API_SETTINGS_SCOPES:
            with tqdm(
                API_SETTINGS_SCOPES[scope], desc="Collections", ncols=180
            ) as collections_pbar:
                for collection in collections_pbar:
                    collections_pbar.set_description(
                        f"{collection} item details in {scope}"
                    )
                    if (
                        len(API_SETTINGS_SCOPES[scope][collection]["mandatorySwitches"])
                        > 0
                    ):
                        # fetches a list of ids from main dump
                        collection_to_fetch = API_SETTINGS_SCOPES[scope][collection][
                            "parent"
                        ]
                        if collection_override is not None:
                            collection_to_fetch += f"_{collection_override}"
                        ids = get_ids(
                            scope=scope,
                            collection=collection_to_fetch,
                            container=container,
                        )
                        with tqdm(
                            ids,
                            desc=f"Currently fetching {scope} {collection} ids",
                            ncols=180,
                        ) as ids_pbar:
                            for xId in ids_pbar:
                                ids_pbar.set_description(
                                    f"Currently fetching {xId.lower()} from {scope}.{collection}"
                                )
                                file_name = f"{collection}_{xId}"
                                item_stream = ctc.get_x_by_id(
                                    scope=scope, collection=collection, item_id=xId
                                )
                                write_json_file(
                                    stream=item_stream,
                                    file_name=file_name,
                                    container=container,
                                    sub_directory=f"{scope}\\{collection}",
                                )
                                ids_pbar.set_description(
                                    f"Currently fetched {len(ids)} ids from {scope}.{collection}"
                                )

    except Exception as err:
        CTCLog(LOG_TITLE).error(str(err))
    finally:
        CTCLog(LOG_TITLE).info("Finished fetching nested collections")
        tqdm._instances.clear()


def get_all_jsons(container: str = CURRENT_DATE_TIME) -> None:
    """Executes a full JSON pull getting both Base and Nested files"""
    get_base_jsons(container=container)
    get_nested_jsons(container=container)


if __name__ == "__main__":
    get_all_jsons()
