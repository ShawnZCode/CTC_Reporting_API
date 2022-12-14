"""A Series of functions allowing the retrieval of data from the CTC CMS API"""

import json
import math
from datetime import date, timedelta

import requests

from JSON.Functions.read_file import read_file

#Current list of constants before settings file is implemented
api_settings = read_file('APICore_Connection\\Settings.json')

rows_per_page = api_settings['apiConnection']['rowsPerPage']
api_env = api_settings['apiConnection']['apiEnv']['Prod']
api_key = api_settings['apiConnection']['reportKey']
day_offset = api_settings['apiConnection']['dayOffset']

def add_switches(scope, collection):
    """Adds relevant switches sourced from api_settings
    REQUIRES: valid api scope and valid collection from scope
    RETURNS: list of switches"""
    switches = ''
    if collection.lower() == 'searches':
        switches += f'&searchedAt={day_offset.strftime("%Y-%m-%d")}'
    switches_list = api_settings['scopes'][scope][collection.lower()]['optionalSwitches']
    for dictionary in switches_list:
        key = list(dictionary.keys())
        switch = key[0]
        value = dictionary[switch]
        switches += f'&{switch}={value}'
    return switches

def get_x_by_id(scope, collection, item_id, added_data=None):
    """retrieves an item record based on the item's id value"""
    switches = add_switches(scope, collection)
    url = f'https://{api_env}.ctcsoftware.com/{scope}/reports/v1/reports/{collection}?reportsKey={api_key}&{collection.lower()}Id={item_id}{switches}'
    response = requests.get(url).text
    data = json.loads(response)
    return data

def get_total_items(scope, collection):
    """Retrieves total count of items by category"""
    switches = add_switches(scope, collection.lower())
    url = f'https://{api_env}.ctcsoftware.com/{scope}/reports/v1/reports/{collection}?reportsKey={api_key}&page=1&pageSize=1{switches}'
    response = requests.get(url).text
    base_data = json.loads(response)
    total_items = int(base_data['totalItems'])
    return total_items

def get_next_x(scope, collection, page_number):
    """Retrieves next X items"""
    switches = add_switches(scope, collection)
    url = f'https://{api_env}.ctcsoftware.com/{scope}/reports/v1/reports/{collection}?reportsKey={api_key}&page={str(page_number).lower()}&pageSize={str(rows_per_page)}{switches}'
    response = requests.get(url).text
    next_json = json.loads(response)
    return next_json

def get_keys(scope, collection, nested_item=""):
    """Used to get the data structure of the json stream"""
    try:
        if collection.lower() == 'searches':
            offset_date = date.today() - timedelta(days=day_offset)
            stream = get_next_x(scope, collection,1)
        else:
            stream = get_next_x(scope, collection,1)
        keys = stream['items'][0].keys()
        return list(keys)
    except Exception as err:
        return err
#test_keys = get_keys('CMS','Contents')

def get_all_x(collection,
              scope='CMS',
              total_rows=None,
              page_number=None,
              previous_items=None):
    """Use to recursively call API to get all <collection> items"""
    if total_rows is None:
        total_rows = int(rows_per_page)
    page_count = math.ceil(int(total_rows)/int(rows_per_page))
    #Establish current page number
    if page_number is None:
        page_number = 1
    else:
        page_number += 1
    #Combine results into single result set
    if previous_items is None:
        total_items = get_next_x(scope, collection, page_number)
    else:
        next_json = get_next_x(scope, collection, page_number)
        for item in next_json['items']:
            previous_items['items'].append(item)
        total_items = previous_items
    #Continue to fetch next page of results
    #Or return final result set
    if page_number < page_count:
        get_all_x(collection, scope, total_rows, page_number, total_items)
    
    return total_items
