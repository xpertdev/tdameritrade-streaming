from tda import auth, client
import json
import config

# authenticate
try:
    c = auth.client_from_token_file(config.TOKEN_PATH, config.API_KEY)
except FileNotFoundError:
    from selenium import webdriver
    chrome_options = webdriver.ChromeOptions()
    if config.CHROME_BINARY:
        chrome_options.binary_location = config.CHROME_BINARY
    with webdriver.Chrome(executable_path=config.CHROMEDRIVER_PATH, options=chrome_options) as driver:
        c = auth.client_from_login_flow(
            driver, config.API_KEY, config.REDIRECT_URI, config.TOKEN_PATH)