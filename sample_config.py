# Sample config file

API_KEY = 'abc'
ACCOUNT_ID = '123456789'
REDIRECT_URI = 'https://localhost'
TOKEN_PATH = '/Users/xpertdev/Projects/tdameritrade-streaming/token.pickle'
CHROMEDRIVER_PATH = '/Users/xpertdev/Projects/tdameritrade-streaming/chromedriver'
#CHROME_BINARY is Optional. Leave blank if using Chrome canary
CHROME_BINARY = ''
QUOTE_PATH = '/Users/xpertdev/Projects/tdameritrade-streaming/Quote/'
SYMBOLS = 'VTI,QQQ,VUG,TQQQ,UPRO'
QUOTE_STORE = 'Azure' # Choose either Azure or Local

#Azure storage
STORAGE_ACCOUNT_NAME = 'STORAGE_ACCOUNT_NAME'
STORAGE_ACCOUNT_KEY  = 'Storage-key'
STORAGE_FILESYSTEM_NAME = 'tdameritradestreamingfilesystem'