import datetime
import quandl
quandl.save_key("Wxxy-x1SEe5XwqKPRDai")

import utils

COLUMNAS = ['Open', 'High', 'Low', 'Close', 'Volume']
LEN_TICKERS = 251

#***************************************************************************************************
#***************************************************************************************************
#***************************************************************************************************
#TODO
def get_ticker_info(ticker, cols, start=datetime.datetime(2017,1,1), end=datetime.datetime(2018,1,1)):

    try:
        hist = quandl.get("BCIW/_IDX", ticker=ticker, start_date=start, end_date=end)

        # get historical market data
        #hist = ticker_info.history(period="max")
        #hist = hist[(hist.index >= start) & (hist.index <= end)]

        return hist
    except ValueError:
        print(ticker + ' does not exists.')
        return None
#***************************************************************************************************
#***************************************************************************************************
#***************************************************************************************************
#print(get_ticker_info('ACM', ''))
#print(len(get_ticker_info('ACM', '')))