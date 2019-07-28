import numpy as np
import requests
from bs4 import BeautifulSoup

COLUMNAS = ['Open', 'High', 'Low', 'Close', 'Volume']

#***************************************************************************************************
#***************************************************************************************************
#***************************************************************************************************
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

#***************************************************************************************************
#***************************************************************************************************
#***************************************************************************************************
def get_returns_turnover(df):

    returns = (df['Close']/df['Open']) - 1
    high_low = (df['High']/df['Low']) - 1
    turnover = df['Close']*df['Volume']

    df['return'] = returns
    df['high_low'] = high_low
    df['turnover'] = turnover

    return df

#***************************************************************************************************
#***************************************************************************************************
#***************************************************************************************************
def sample_mean(df, cols):

    return df[[cols]].mean(axis=0)

#TODO rango fechas
def sample_variance(df, cols):

    return -1

#TODO
def standard_deviation(df_yahoo, df_quandl, cols):

    return -1