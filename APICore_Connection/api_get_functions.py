"""A Series of functions allowing the retrieval of data from the CTC CMS API"""

#from dotenv import load_dotenv
import json
import math
from datetime import date, datetime, timedelta
from time import perf_counter, sleep
from JSON.read_file import read_file
import requests

#load_dotenv()

## Current list of constants before settings file is implemented
api_settings = read_file("APICore_Connection\\Settings.json")

rows_per_page = api_settings["apiConnection"]["rowsPerPage"]
api_env = api_settings["apiConnection"]["apiEnv"]["Prod"]
api_key = api_settings["apiConnection"]["reportKey"]
day_offset = api_settings["apiConnection"]["dayOffset"]

## Switch Builder used to assemble the Connection URL
def add_switches(scope, collection):
    """Adds relevant switches sourced from api_settings
    REQUIRES: valid api scope and valid collection from scope
    RETURNS: list of switches"""
    switches = ""
    try:
        switches_list = api_settings["scopes"][scope][collection.lower()][
            "optionalSwitches"
        ]
        for dictionary in switches_list:
            key = list(dictionary.keys())
            switch = key[0]
            value = dictionary[switch]
            switches += f"&{switch}={value}"
    except Exception as err:
        switches = ""
        return err
    finally:
        return switches

## Define the URL generator
def gen_url(
    scope: str,
    collection: str,
    item_id: str=None,
    page_number: int=None,
    rowsPerPage: int=None,
    start_date: str=None,
    end_date: str=None,
    switches: str=None,
):
    """generates the URL needed for navigation"""
    url_pre = f"https://{api_env}.ctcsoftware.com/{scope}/reports/v1/reports/{collection}?reportsKey={api_key}"

    ##Collection handling
    if collection == "app-sessions":
        col = "product"
    elif collection == "doc-session":
        col = "session"
    else:
        col = collection

    ##Id handling
    if item_id != None:
        url_id = f"&{col}Id={item_id}"
    else:
        url_id = ""

    ##Page handling
    if rowsPerPage != None:
        rpp = str(rowsPerPage)
    else:
        rpp = str(rows_per_page)

    if page_number != None:
        if collection != "app_sessions":
            url_page = f"&page={str(page_number)}&pageSize={rpp}"
        else:
            url_page = ""
    else:
        url_page = ""

    ##Date handling
    col = collection.lower()
    if (
        col == "searches"
        or col == "app-sessions"
        or col == "doc-sessions"
        or col == "sessions"
    ) and start_date == None:
        current_date = date.today() - timedelta(day_offset)
        date_str = current_date.strftime("%Y-%m-%d")
        start_date = date_str

    if (
        col == "app-sessions" or col == "doc-sessions" or col == "sessions"
    ) and end_date == None:
        current_date = date.today() + timedelta(1)
        date_str = current_date.strftime("%Y-%m-%d")
        end_date = date_str

    if col == "searches":
        url_date = f"&searchedAt={start_date}"
    elif col == "app-sessions" or col == "doc-sessions" or col == "sessions":
        if start_date != None and end_date != None:
            url_date = f"&startDate={start_date}&endDate={end_date}"
        elif start_date != None and end_date == None:
            url_date = f"&startDate={start_date}"
        elif start_date == None and end_date != None:
            url_date = f"&endDate={end_date}"
        else:
            url_date = ""
    else:
        url_date = ""

    ##Switches handling
    if switches != None:
        url_switches = f"&{switches}"
    else:
        url_switches = ""

    url = f"{url_pre}{url_id}{url_date}{url_page}{url_switches}"

    return url

## Calls CTC Reporting API to get items by ID
def get_x_by_id(scope, collection, item_id, added_data=None):
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
        #sleep(response_end - response_start)
    except Exception as err:
        data = {}
    finally:
        return data

## Calls CTC Reporting API to get total items for a given collection
def get_total_items(scope, collection):
    """Retrieves total count of items by category"""
    switches = add_switches(scope, collection.lower())
    url = gen_url(
        scope = scope,
        collection=collection,
        page_number=1,
        rowsPerPage=1,
        switches=switches,
    )
    try:
        response_start = perf_counter()
        response = requests.get(url).text
        base_data = json.loads(response)
        total_items = int(base_data["totalItems"])
        response_end = perf_counter()
        # sleep(response_end - response_start)
    except Exception as err:
        total_items = None
    finally:
        return total_items

## Calls CTC Reporting API to get next X items
def get_next_x(scope, collection, page_number):
    """Retrieves next X items"""
    switches = add_switches(scope, collection)
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
    return next_json


def get_keys(scope: str, collection: str):
    """Used to get the data structure of the json stream"""
    try:
        stream = get_next_x(scope, collection, 1)
        keys = stream["items"][0].keys()
        return list(keys)
    except Exception as err:
        return err


# test_keys = get_keys('CMS','Contents')

## Calls the CTC Reporting API to get all items in a collection
    ## Uses the get_next_x function to recursively call the API to get all items
def get_all_x(
    scope: str,
    collection: str,
    total_rows: int = None,
    page_number: int = None,
    previous_items=None,
):
    """Use to recursively call API to get all <collection> items"""
    if total_rows is None:
        total_rows = int(rows_per_page)
    page_count = math.ceil(int(total_rows) / int(rows_per_page))
    # Establish current page number
    if page_number is None:
        page_number = 1
    else:
        page_number += 1
    # Combine results into single result set
    if previous_items is None:
        total_items = get_next_x(scope, collection, page_number)
    else:
        next_json = get_next_x(scope, collection, page_number)
        for item in next_json["items"]:
            previous_items["items"].append(item)
        total_items = previous_items
    # Continue to fetch next page of results
    # Or return final result set
    if page_number < page_count:
        get_all_x(scope, collection, total_rows, page_number, total_items)

    return total_items
