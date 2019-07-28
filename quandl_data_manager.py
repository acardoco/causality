import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import datetime
import time
import quandl as ql

import utils

COLUMNAS = ['Open', 'High', 'Low', 'Close', 'Volume']
LEN_TICKERS = 251