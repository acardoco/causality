import numpy as np
import pandas as pd
import yfinance as yf
import requests
from bs4 import BeautifulSoup

def get_SP_400():

    website = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_400_companies')

    soup = BeautifulSoup(website, 'html')





def get_ticker_info(ticker, cols, start="2017-01-01", end="2018-01-01"):

    ticker_info = yf.Ticker(ticker)

    # get stock info
    stock = ticker_info.info

    # get historical market data
    hist = ticker_info.history(period="max")
    hist = hist.reset_index()

    hist = hist[
        (hist['Date'] >= start) &
        (hist['Date'] <= end) ]
    return hist[cols], stock

def save_info(list400):

    cols = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    for ele in list400:
        info = get_ticker_info('ticker', cols)

hist, stock = get_ticker_info('ACHC',['Date', 'Open', 'High', 'Low', 'Close', 'Volume'],'','')
print(stock)
print(hist.head())
#get_SP_400()