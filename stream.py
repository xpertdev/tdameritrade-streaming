from tda.auth import easy_client
from tda.client import Client
from tda.streaming import StreamClient

import asyncio
import json
import config
import os
import file_helper as fileHelper

client = easy_client(
        api_key=config.API_KEY,
        redirect_uri=config.REDIRECT_URI,
        token_path=config.TOKEN_PATH)
stream_client = StreamClient(client, account_id=config.ACCOUNT_ID)

def level1_order_book_handler(msg):
    write_to_file(msg, fileHelper.FileType.Level1)

def nasdaq_order_book_handler(msg):
    write_to_file(msg, fileHelper.FileType.Level2)

def timesale_order_book_handler(msg)    :
    write_to_file(msg, fileHelper.FileType.TimeSale)

def write_to_file(msg, fileType):
    fileType = fileHelper.FileType(fileType)
    file_name = fileHelper.get_filename(fileType)
    folder_name = os.path.join(config.QUOTE_PATH, fileType.name)
    file_path = os.path.join(folder_name, file_name)

    fileHelper.create_folder(folder_name)
    fileHelper.write_file(msg, file_path)
    print(file_name)

async def read_stream():
    await stream_client.login()
    await stream_client.quality_of_service(StreamClient.QOSLevel.DELAYED)
    
    #register level1 handler
    stream_client.add_level_one_equity_handler(level1_order_book_handler)
    await stream_client.level_one_equity_subs([config.SYMBOLS])

    #register level2 handler
    stream_client.add_nasdaq_book_handler(nasdaq_order_book_handler)
    await stream_client.nasdaq_book_subs([config.SYMBOLS])

    #register time of sale handler
    stream_client.add_timesale_equity_handler(timesale_order_book_handler)
    await stream_client.timesale_equity_subs([config.SYMBOLS])

    while True:
        await stream_client.handle_message()

asyncio.run(read_stream())
#asyncio.get_event_loop().run_until_complete(read_stream())