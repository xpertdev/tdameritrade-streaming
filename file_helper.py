from enum import Enum

import time
import json
import os


class FileType(Enum):
    Level1 = 1
    Level2 = 2
    TimeSale = 3

def get_filename(fileType):
    epoch_time = str(time.time())
    fileType = FileType(fileType)
    return epoch_time + "-" + fileType.name + ".json"

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def write_file(msg, file_path):
    #short_date = datetime.today().strftime('%Y-%m-%d')
    with open(file_path, "w") as file1:
        #content = input(json.dumps(msg, indent=4))
        content = json.dumps(msg)
        file1.write(content)