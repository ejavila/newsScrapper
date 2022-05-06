# Importing the requests and pandas libraries.
import requests
import pandas as pd


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
baseUrl = 'https://finviz.com/quote.ashx?t='
# Creating a list of tickers.
tickers = ['AAPL','MSFT','AMZN','GOOGL','FB','INTC','CSCO','NVDA','NFLX','TSLA','AMAT','ADBE','ADI','ADP','ADSK','AKAM','ALGN','ALXN','AMAT','AMGN','AMZN','APHA','APOG','ARIA','ARNA','ASML','ATVI','AVGO','AWK','AXP','AZN','BA','BABA','BAC','BAX','BBT','BDX','BIDU','BIIB','BKNG','BLK','BMRN','BMY','BRCM','BRK.B','BSX','BWA','CA','CAFE','CAMT','CAT','CB','CCI','CDNS','CDW','CERN','CHKP','CHTR','CI','CL','CLDR','CLF','CLVS','CMCSA','CME','CNC','CNP','COF','COG','COST','COTY','COUP','CPB','CRM','CRSP','CSC','CSX','CTAS','CTSH','CTXS','CTXS','CVS','CVX','CXO','D','DAL','DD','DE','DELL','DG','DGX','DHI','DHR','DIS','DISCA','DISCK','DISH','DLR','DLTR','DNR','DOV','DRE','DRI','DTE','DUK','DVN','DXC','EA','EBAY','ECL','ED','EFX','EIX','EL','EMC','EMN','EMR','EOG','EQIX','EQR','EQT','ESRX','ESV','ETN','ETR','EW','EXC','EXPD','EXPE','EXR','F','FAST','FB','FCC','FDT','FDX','FE','FIS','FISV','FITB','FLIR','FLR','FLS','FMC','FOSL','FOXA','FOXA','FOX','FOXA','FRT','FTI','FTR','GAS','GD','GE','GILD','GIS','GLW','GM','GME','GNW','GOOG']


# Getting the current date and formatting it to a string.
today = pd.datetime.today().strftime('%d%b')

def getHtml(url, ticker):
    """
    It takes a URL and a ticker symbol as input, and then it uses the requests library to get the HTML
    from the URL, and then it writes the HTML to a file.
    
    :param url: the url of the website you want to scrape
    :param ticker: the stock ticker symbol
    """
    r = requests.get(url + ticker, headers=headers)
    with open('datasets/' + ticker + '_' + str.lower(today) + '.html', 'wb') as f:
        f.write(r.content)

# Looping through the tickers list and calling the getHtml function for each ticker.
for ticker in tickers:
    getHtml(baseUrl, ticker)

