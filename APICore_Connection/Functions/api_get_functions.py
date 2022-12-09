"""A Series of functions allowing the retrieval of data from the CTC CMS API"""

from datetime import date, timedelta
import json
import math
import requests
from JSON.Functions.read_file import read_file

#Current list of constants before settings file is implemented
api_settings = read_file('APICore_Connection\\Settings.json')

rows_per_page = api_settings['CTCAPI']['rowsPerPage']
api_env = api_settings['CTCAPI']['apiEnv']['Prod']
api_key = api_settings['CTCAPI']['reportKey']
day_offset = api_settings['CTCAPI']['dayOffset']

def add_switches(collection, switches):
    if collection.lower() == 'searches':
        if switches is None:
            offset_date = date.today() - timedelta(days=day_offset)
            switches = f'&searchedAt={offset_date.strftime("%Y-%m-%d")}'
        else:
            switches = f'&searchedAt={offset_date.strftime("%Y-%m-%d")}&{switches}'
    else:
        if switches is None:
            switches = ''
        else:
            switches = f'&{switches}'
    return switches

def get_x_by_id(route, collection, item_id, added_data=None):
    """retrieves an item record based on the item's id value"""
    switches = add_switches(collection, added_data)
    url = f'https://{api_env}.ctcsoftware.com/{route}/reports/v1/reports/{collection}?reportsKey={api_key}&{collection.lower()}Id={item_id}{switches}'
    response = requests.get(url).text
    data = json.loads(response)
    return data

def get_total_items(route, collection, added_switches=None):
    """Retrieves total count of items by category"""
    add_switch = add_switches(collection, added_switches)
    url = f'https://{api_env}.ctcsoftware.com/{route}/reports/v1/reports/{collection}?reportsKey={api_key}&page=1&pageSize=1{add_switch}'
    response = requests.get(url).text
    base_data = json.loads(response)
    total_items = int(base_data['totalItems'])
    return total_items

def get_next_x(route, collection, page_number, added_switches=None):
    """Retrieves next X items"""
    add_switch = add_switches(collection, added_switches)
    url = f'https://{api_env}.ctcsoftware.com/{route}/reports/v1/reports/{collection}?reportsKey={api_key}&page={str(page_number).lower()}&pageSize={str(rows_per_page)}{add_switch}'
    response = requests.get(url).text
    next_json = json.loads(response)
    return next_json

def get_keys(route, collection, nested_item=""):
    """Used to get the data structure of the json stream"""
    try:
        if collection.lower() == 'searches':
            offset_date = date.today() - timedelta(days=day_offset)
            stream = get_next_x(route, collection,1,f'searchedAt={offset_date.strftime("%Y-%m-%d")}')
        else:
            stream = get_next_x(route, collection,1)
        keys = stream['items'][0].keys()
        return list(keys)
    except Exception as err:
        return err
#test_keys = get_keys('CMS','Contents')

def get_all_x(collection,
              route='CMS',
              total_rows=None,
              page_number=None,
              previous_items=None,
              added_switches=None):
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
        total_items = get_next_x(route, collection, page_number, added_switches)
    else:
        next_json = get_next_x(route, collection, page_number, added_switches)
        for item in next_json['items']:
            previous_items['items'].append(item)
        total_items = previous_items
    #Continue to fetch next page of results
    #Or return final result set
    if page_number < page_count:
        get_all_x(collection, route, total_rows, page_number, total_items, added_switches)
    
    return total_items
