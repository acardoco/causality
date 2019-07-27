import numpy as np
import pandas as pd
import yfinance as yf
import requests
from bs4 import BeautifulSoup

def get_SP_400():

    website = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_400_companies')

    soup = BeautifulSoup(website, 'html')





def get_ticker_info(ticker, cols, start, end):

    ticker_info = yf.Ticker(ticker)

    # get stock info
    stock = ticker_info.info

    # get historical market data
    hist = ticker_info.history(period="max")

    return hist[['Open', 'High', 'Low', 'Close', 'Volume']], stock

'''hist, stock = get_ticker_info('ACHC','','','')
print(stock)
print(hist.head())'''
get_SP_400()