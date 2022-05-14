# -*- coding: utf-8 -*-
"""
Created on Thu May 12 13:25:21 2022

@author: loklu
"""


import pandas as pd
import yfinance as yf
#from yahoofinancials import YahooFinancials

def stockdata(stock):
    data = yf.download(stock)
    ticker = yf.Ticker(stock)
    data_df = ticker.history(period="7d",interval=("5m"))
    data_df['Close'].plot(title="TSLA's stock price")
    return data_df

stockdata('TSLA')