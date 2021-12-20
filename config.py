import json
from sys import platform
import getpass
import os

def _get_batch_from_local():
    AYLIEN_BATCH_NUMBER = 1
    try:
        batch_filename = 'aylien_batch_number.txt'
        if not os.path.isfile(batch_filename) :
            file = open(batch_filename, 'w+')
            file.write('1')
        else:
            file = open(batch_filename, 'r')
            AYLIEN_BATCH_NUMBER = file.read() 
            AYLIEN_BATCH_NUMBER = int(AYLIEN_BATCH_NUMBER) + 1
            file = open(batch_filename, 'w')
            file.write(str(AYLIEN_BATCH_NUMBER))
    except (Exception) as error:
        print(error)
    return AYLIEN_BATCH_NUMBER

_config = {}

user = getpass.getuser()
if (platform == "linux" or platform == "linux2") and user != "rachel":
    _environment = 'production'
else:
    _environment = 'development'

# with open("config.json", "r") as read_file:
#     parsed_config = json.load(read_file)
#     if _environment == 'production':
#         _config = parsed_config['PROD']
#     else:
#         _config = parsed_config['DEV']


class Config(object):
    ENVIRONMENT = _environment
    # API_KEY = _config.get('API_KEY')
    # UVICORN_PORT = _config.get('UVICORN_PORT') or 5000
    # DB_USER = _config.get("DB_USER")
    # DB_PASSWORD = _config.get("DB_PASSWORD")
    # DB_HOST = _config.get("DB_HOST")
    # DB_DATABASE = _config.get("DB_DATABASE")
    # DB_PORT = _config.get("DB_PORT") or 5432
    # AYLIEN_APP_ID = _config.get("AYLIEN_APP_ID")
    # AYLIEN_APP_KEY = _config.get("AYLIEN_APP_KEY")
    # NEW_AYLIEN_APP_ID = _config.get("NEW_AYLIEN_APP_ID")
    # NEW_AYLIEN_APP_KEY = _config.get("NEW_AYLIEN_APP_KEY")
    # AYLIEN_TEXT_ID = _config.get("AYLIEN_TEXT_ID")
    # AYLIEN_TEXT_KEY = _config.get("AYLIEN_TEXT_KEY")
    # CLUSTER_THRESHOLD = _config.get("CLUSTER_THRESHOLD")
    # LIMIT_STORIES_DOWNLOAD = _config.get("LIMIT_STORIES_DOWNLOAD")
    # CLUSTER_HOURS_LOOKBACK = _config.get("CLUSTER_HOURS_LOOKBACK")
    # TOPIC_BATCH_SIZE = _config.get("TOPIC_BATCH_SIZE")
    PLACEHOLDER = "fetched using text api: not available"
    AYLIEN_BATCH_NUMBER = _get_batch_from_local()
