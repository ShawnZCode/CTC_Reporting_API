# import Modules.Groups
# import Modules.Roles
from JSON.create_json_cache_files import get_base_jsons, json_settings
from JSON.read_file import read_file
from SQL_Connection.db_main import create_all, drop_all
from z_DB_API_Connector.Modules.Refreshed import create_refreshed, fetch_last_refreshed
from z_DB_API_Connector.Modules.Users import create_update_users

root_path = json_settings["files"]["storageCachePath"]

# SQL Testing
# drop_all()
create_all()

last_refreshed = create_refreshed()
# last_refreshed = fetch_last_refreshed()
get_base_jsons(container=last_refreshed.id)

users_json_path: str = f"{root_path}/{last_refreshed.id}/Accounts/Users.json"
user_items: dict = read_file(users_json_path)["items"]
create_update_users(items=user_items)
