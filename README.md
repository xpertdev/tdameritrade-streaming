# tdameritrade-streaming

Streaming order book data from TD Ameritrade API. Save json either to local disk or Azure Data Lake Storage Gen2. I have this script running 24/7 on a  Microsoft Azure VM for a few months now.

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
- Refer to json files in the Quote folder

Support for Docker coming soon.

## Uses the tda-api Python Package

https://tda-api.readthedocs.io/

### Upgrading tda-api

If you already had tda-api installed, make sure you upgrade to the latest version!

```
pip install --upgrade -r requirements.txt
```

## Video tutorial

https://youtube.com/parttimelarry

Original code from https://github.com/hackingthemarkets/tdameritrade-streaming