import numpy as np
import pandas as pd
import yfinance as yf
import requests
from bs4 import BeautifulSoup
import datetime
import time

COLUMNAS = ['Open', 'High', 'Low', 'Close', 'Volume']

def get_SP_400():

    website = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_400_companies').text
    soup = BeautifulSoup(website, 'lxml')
    tabla = soup.find('table', {'class': 'wikitable sortable'})
    lista_tickers = tabla.findAll("a", {"class": "external text"})

    lista_final_sticker = []
    for ticker in lista_tickers:
        t = ticker.string
        if t != 'reports':
            lista_final_sticker.append(t)

    print(len(lista_final_sticker))
    return np.asarray(lista_final_sticker)


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

    list400 = get_SP_400()

    i = 0
    start_time = time.time()
    for ele in list400:
        print(ele)
        info = get_ticker_info(ele, COLUMNAS)
        i+=1
        print(i)
    end_time = time.time()
    print('Download info time:', end_time-start_time)

#hist, stock = get_ticker_info('ACHC',COLUMNAS,'','')
#print(hist.head())
#get_SP_400()
save_info()