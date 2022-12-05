"""'Quick' test of json_cache_files.py"""

#from JSON.Classes import json_cache_files

from APICore_Connection.Classes import api_get_functions as ctc
from JSON import read_file

ctc.get_all_x('CMS', 'Contents',1)
#json_cache_files.get_base_jsons()
#json_cache_files.get_nested_jsons()
