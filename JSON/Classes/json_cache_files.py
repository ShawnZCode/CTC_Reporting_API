"""Routines to generate the local cache files from the CTC API"""

import os
from datetime import datetime
import time
import json
from APICore_Connection.Classes import api_get_functions as ctc
from JSON.read_file import read_file

BASE_FILE_LIST = ['Contents', 'Libraries', 'Saved-Searches', 'Searches', 'Tags']

settings = read_file('APICore_Connection\\Settings.json')
base_file_dict = read_file('SQL_Connection\\SupportFiles\\Files_Collection_Deprecated.json')

def directory_create(current_date_time):
    """Ensures a directory for current date time cache of files"""
    try:
        setting = settings['files']['storageCachePath']
        root_directory = f'{setting}\\{current_date_time}'
        os.makedirs(root_directory, exist_ok=True)
        return root_directory
    except Exception as err:
        return err

current_date_time=datetime.now().strftime('%Y-%m-%d_%H-%M')

def write_json_file(stream, file_name, sub_directory='CMS'):
    """Writes a json file from streamed data"""
    try:
        file_path = f'{directory_create(current_date_time)}\\{sub_directory}'
        os.makedirs(file_path, exist_ok=True)
    except:
        pass
    try:
        file_path += f'\\{file_name}.json'
        with open(file_path, 'w') as f:
            #f.write(json.dumps(stream, indent=4))
            json.dump(stream, f, indent = 4)
            print(f'Saved {file_path}')
    except Exception as err:
        print(err)

def get_base_jsons(route='CMS'):
    """Writes the original Json Files"""
    try:
        for key in base_file_dict.keys():
            write_json_file(ctc.get_all_x(key, route, ctc.get_total_items(route, key)), key, route)
    except Exception as err:
        return err
    try:
        get_nested_jsons()
    except Exception as err:
        return err

def get_ids(collection, sub_directory='CMS'):
    """Parse the Json file and returns a list of ids"""
    try:
        file_path = f'{directory_create(current_date_time)}\\{sub_directory}'
        file_path += f'\\{collection}.json'
        with open(file_path, 'r') as f:
            stream = json.loads(f.read())
    except Exception as err:
        print(err)
    try:
        ids = []
        for i in stream['items']:
            ids.append(i['id'])
        return ids
    except Exception as err:
        return err

def get_nested_jsons():
    """Writes the original Json Files"""
    try:
        for key in base_file_dict.keys():
            if key != 'Saved-Searches':
                ids = get_ids(key, 'CMS')
                nested = base_file_dict[key]['nested']
                switches = base_file_dict[key]['switches']
                try:
                    for id in ids:
                        file_name = f'{nested}_{id}'
                        write_json_file(ctc.get_x_by_id(nested, id, switches), file_name, f'CMS\\{nested}')
                except Exception as err:
                    return err
    except Exception as err:
        return err

#start_time = time.perf_counter()

# get_base_jsons()

# finish_time = time.perf_counter()
# total_time = round(finish_time-start_time, 2)
# print(f'Json files finished in {total_time} seconds(s) or {total_time/60} minute(s)')
