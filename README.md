# tdameritrade-streaming

Stream order book data using TD Ameritrade API. Supports Level 1, Level 2 and Time of Sale. Save quotes either to your local disk or Azure Data Lake Storage Gen2. I have this script running 24/7 on a  Microsoft Azure VM for a few months now.

## Instructions

- Rename the file sample_config.py to config.py.
- Customize config.py per your needs. See the video tutorial for instructions to create TD Ameritrade API key and token.
- Start the program. Dependencies are automatically installed. Script restarts if there are any errors.
- To stop, kill the process.

## Start

```
./start.sh
```

## Sample Data
- Refer to json files in the [Quote folder](https://github.com/xpertdev/tdameritrade-streaming/tree/master/Quote "Quote")

Support for Docker coming soon.

## Dependencies

[tda-api](https://github.com/alexgolec/tda-api "tda-api")

### Upgrading Dependencies

If you already had tda-api installed, make sure you upgrade to the latest version!

```
pip install --upgrade -r requirements.txt
```

## Video tutorial

https://youtube.com/parttimelarry

Original code: https://github.com/hackingthemarkets/tdameritrade-streaming
