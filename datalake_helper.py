import time
import json
import os, uuid
import config
from azure.storage.filedatalake import (DataLakeServiceClient,)
from enum import Enum

storage_account_name = config.STORAGE_ACCOUNT_NAME
storage_account_key = config.STORAGE_ACCOUNT_KEY
storage_filesystem_name = config.STORAGE_FILESYSTEM_NAME

# set up the service client with the credentials from the environment variables
service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
    "https",
    storage_account_name
), credential=storage_account_key)

# get the filesystem
file_system_client = service_client.get_file_system_client(file_system=storage_filesystem_name)

class FileType(Enum):
    Level1 = 1
    Level2 = 2
    TimeSale = 3

def get_filename(fileType):
    epoch_time = str(time.time())
    fileType = FileType(fileType)
    return "{}-{}.json".format(epoch_time, fileType.name)

def write_file(msg, folder_name, file_name):
    
    directory_client = file_system_client.get_directory_client(folder_name)
    if not directory_client.exists():
        directory_client.create_directory()
        
    file_client = directory_client.create_file(file_name)

    content = json.dumps(msg)
    file_client.append_data(content, 0, len(content))
    file_client.flush_data(len(content))
