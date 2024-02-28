"""A Series of functions allowing the retrieval of data from the CTC CMS API"""

# from dotenv import load_dotenv
import json
import math
from datetime import date, datetime, timedelta
from time import perf_counter, sleep

import models
import requests
from base_models import Collection, Scope, Scopes

from Logging.ctc_logging import CTCLog
from utils.read_file import read_file

# load_dotenv()
## Current list of constants before settings file is implemented
API_SETTINGS = read_file("APICore_Connection\\Settings.json")

ROWS_PER_PAGE = API_SETTINGS["apiConnection"]["rowsPerPage"]
API_ENV = API_SETTINGS["apiConnection"]["apiEnv"]["Prod"]
API_KEY = API_SETTINGS["apiConnection"]["reportKey"]
DAY_OFFSET = API_SETTINGS["apiConnection"]["dayOffset"]
LOG_TITLE = API_SETTINGS["logTitle"]


## Switch Builder used to assemble the Connection URL
def add_switches(collection: Collection) -> str:
    """Adds relevant switches sourced from API_SETTINGS
    REQUIRES: valid api scope and valid collection from scope
    RETURNS: list of switches"""
    switches = ""
    try:
        switches_list = collection.optional_switches
        for dictionary in switches_list:
            key = list(dictionary.keys())
            switch = key[0]
            value = dictionary[switch]
            switches += f"&{switch}={value}"
    except Exception as err:
        switches = ""
        raise err
    finally:
        return switches


## Define the URL generator
def gen_url(
    scope: Scope,
    collection: Collection,
    item_id: str = None,
    page_number: int = None,
    int_rows_per_page: int = None,
    start_date: str = None,
    end_date: str = None,
    switches: str = None,
) -> str:
    """generates the full URL needed for any requested route"""

    url_pre = f"https://{API_ENV}.ctcsoftware.com/{scope.name}/reports/v1/reports/{col_name}?reportsKey={API_KEY}"
    col_name = collection.name
    ##Collection handling
    if col_name == "app-sessions":
        col = "product"
    elif col_name == "doc-session":
        col = "session"
    else:
        col = col_name

    ##Id handling
    if item_id is not None:
        url_id = f"&{col}Id={item_id}"
    else:
        url_id = ""

    ##Page handling
    if int_rows_per_page is not None:
        rpp = str(int_rows_per_page)
    else:
        rpp = str(ROWS_PER_PAGE)

    if page_number is not None:
        if col_name != "app_sessions":
            url_page = f"&page={str(page_number)}&pageSize={rpp}"
        else:
            url_page = ""
    else:
        url_page = ""

    ##Date handling
    col = col_name.lower()
    if (
        col == "searches"
        or col == "app-sessions"
        or col == "doc-sessions"
        or col == "sessions"
    ) and start_date is None:
        current_date = date.today() - timedelta(DAY_OFFSET)
        date_str = current_date.strftime("%Y-%m-%d")
        start_date = date_str

    if (
        col == "app-sessions" or col == "doc-sessions" or col == "sessions"
    ) and end_date is None:
        current_date = date.today() + timedelta(1)
        date_str = current_date.strftime("%Y-%m-%d")
        end_date = date_str

    if col == "searches":
        url_date = f"&searchedAt={start_date}"
    elif col == "app-sessions" or col == "doc-sessions" or col == "sessions":
        if start_date is not None and end_date is not None:
            url_date = f"&startDate={start_date}&endDate={end_date}"
        elif start_date is not None and end_date is None:
            url_date = f"&startDate={start_date}"
        elif start_date is None and end_date is not None:
            url_date = f"&endDate={end_date}"
        else:
            url_date = ""
    else:
        url_date = ""

    ##Switches handling
    if switches is not None:
        url_switches = f"&{switches}"
    else:
        url_switches = ""

    url = f"{url_pre}{url_id}{url_date}{url_page}{url_switches}"
    return url


## Calls CTC Reporting API to get items by ID
def get_x_by_id(
    scope: Scope, collection: Collection, item_id: set, added_data: str = None
) -> dict:
    """retrieves an item record based on the item's id value"""
    try:
        switches = add_switches(scope, collection)
        url = gen_url(
            scope=scope, collection=collection, item_id=item_id, switches=switches
        )
        response_start = perf_counter()
        response = requests.get(url).text
        data = json.loads(response)
        response_end = perf_counter()
        # sleep(response_end - response_start)
    except Exception as err:
        data = {}
        raise err
    finally:
        return data


## Calls CTC Reporting API to get total items for a given collection
def get_total_items(scope: Scope, collection: Collection) -> int:
    """Retrieves total count of items by category"""
    CTCLog(LOG_TITLE).info(
        f"Fetching total item count for {scope.name} {collection.name}"
    )
    switches: str = add_switches(scope, collection)
    url: str = gen_url(
        scope=scope,
        collection=collection,
        page_number=1,
        int_rows_per_page=1,
        switches=switches,
    )
    try:
        response_start = perf_counter()
        response: dict = requests.get(url).text
        base_data: dict = json.loads(response)
        total_items: int = int(base_data["totalItems"])
        response_end = perf_counter()
        # sleep(response_end - response_start)
        CTCLog(LOG_TITLE).info(
            f"Successfully fetched {total_items} as item count from {url}"
        )
    except Exception as err:
        total_items = None
        raise err
    finally:
        return total_items


## Calls CTC Reporting API to get next X items
def get_next_x(scope: Scope, collection: Collection, page_number: int) -> dict:
    """Retrieves next X items"""
    switches = add_switches(scope=scope, collection=collection)
    url = gen_url(
        scope=scope, collection=collection, page_number=page_number, switches=switches
    )
    try:
        response_start = perf_counter()
        response = requests.get(url).text
        next_json = json.loads(response)
        response_end = perf_counter()
        # sleep(response_end - response_start)
    except Exception as err:
        next_json = None
        raise err
    return next_json


def get_keys(scope: Scope, collection: Scope) -> list[str]:
    """Used to get the data structure of the json stream"""
    try:
        stream = get_next_x(scope=scope, collection=collection, page_number=1)
        keys = stream["items"][0].keys()
        return list(keys)
    except Exception as err:
        raise err


## Calls the CTC Reporting API to get all items in a collection
## Uses the get_next_x function to recursively call the API to get all items
def get_all_x(
    scope: Scope,
    collection: Collection,
    total_rows: int = None,
    page_number: int = None,
    previous_items: list[dict] = None,
) -> list[dict]:
    """Use to recursively call API to get all <collection> items"""
    if total_rows is None:
        total_rows = int(ROWS_PER_PAGE)
    page_count = math.ceil(int(total_rows) / int(ROWS_PER_PAGE))
    # Establish current page number
    if page_number is None:
        page_number = 1
    else:
        page_number += 1
    # Combine results into single result set
    if previous_items is None:
        total_items = get_next_x(
            scope=scope, collection=collection, page_number=page_number
        )
    else:
        next_json = get_next_x(
            scope=scope, collection=collection, page_number=page_number
        )
        for item in next_json["items"]:
            previous_items["items"].append(item)
        total_items = previous_items
    # Continue to fetch next page of results
    # Or return final result set
    if page_number < page_count:
        get_all_x(
            scope=scope,
            collection=collection,
            total_rows=total_rows,
            page_number=page_number,
            previous_items=total_items,
        )
    return total_items
