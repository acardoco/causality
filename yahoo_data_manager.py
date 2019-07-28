import numpy as np
import pandas as pd
import yfinance as yf
import requests
from bs4 import BeautifulSoup
import datetime
import time

import utils

COLUMNAS = ['Open', 'High', 'Low', 'Close', 'Volume']
LEN_TICKERS = 251


def get_ticker_info(ticker, cols, start=datetime.datetime(2017,1,1), end=datetime.datetime(2018,1,1)):

    try:
        ticker_info = yf.Ticker(ticker)

        # get historical market data
        hist = ticker_info.history(period="max")
        hist = hist[(hist.index >= start) & (hist.index <= end)]

        return hist[cols]
    except ValueError:
        print(ticker + ' does not exists.')
        return None


def save_info():

    list400 = utils.get_SP_400()

    i = 1
    start_time = time.time()
    np_returns = np.zeros((LEN_TICKERS, 401))
    np_highLow = np.zeros((LEN_TICKERS, 401))
    np_turnover = np.zeros((LEN_TICKERS, 401))
    erroneos = 0
    dif_shape = 0
    for ele in list400:
        print(ele)
        info = get_ticker_info(ele, COLUMNAS)
        if isinstance(info, pd.DataFrame) and info.shape[0] == LEN_TICKERS:
            info = utils.get_returns_turnover(info)
            print(info.shape)
            np_returns[:, i] = info['return']
            np_highLow[:, i] = info['high_low']
            np_turnover[:, i] = info['turnover']

        else:
            if isinstance(info, pd.DataFrame):
                if info.shape[0] > 0:
                    dif_shape += 1
            np_returns[:, i] = np.zeros((LEN_TICKERS))
            np_highLow[:, i] = np.zeros((LEN_TICKERS))
            np_turnover[:, i] = np.zeros((LEN_TICKERS))
            erroneos += 1
        i+=1
        print(i)

    end_time = time.time()
    print('Download info time:', end_time-start_time)
    print('Empties:', erroneos)
    print('Diff shape:', dif_shape)

    dates = [dt.strftime("%Y%m%d") for dt in get_ticker_info('AAN', COLUMNAS).index]
    np_returns[:, 0] = dates
    np_highLow[:, 0] = dates
    np_turnover[:, 0] = dates

    cols_df = np.insert(list400, 0, 'Date')

    df_return = pd.DataFrame(np_returns, columns=cols_df)
    df_highLow = pd.DataFrame(np_highLow, columns=cols_df)
    df_turnover = pd.DataFrame(np_turnover, columns=cols_df)

    print(df_return.head())

    df_return.to_csv('outputs/yahoo__return.csv', index=False)
    df_highLow.to_csv('outputs/yahoo__high_low.csv', index=False)
    df_turnover.to_csv('outputs/yahoo__turnover.csv', index=False)


#hist, stock = get_ticker_info('ACHC',COLUMNAS,'','')
#print(hist.head())
#get_SP_400()
save_info()