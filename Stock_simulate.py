# -*- coding: utf-8 -*-
"""
Created on Thu May 12 13:25:21 2022

@author: loklu
"""


import pandas as pd
import yfinance as yf
from yahoo_fin import stock_info as si
#from yahoofinancials import YahooFinancials

def stockdata(stock):
    ticker = yf.Ticker(stock)
    data_df = ticker.history(period="60d",interval=("5m"))
    #data_df['Close'].plot(title="TSLA's stock price")
    return data_df

#stockdata('TSLA')

def stock_names():
    # get most important datas
    df1 = pd.DataFrame( si.tickers_sp500() )
    df2 = pd.DataFrame( si.tickers_nasdaq() )
    df3 = pd.DataFrame( si.tickers_dow() )
    df4 = pd.DataFrame( si.tickers_other() )

    # Get to sets to make sure things does not overlap
    sym1 = set( symbol for symbol in df1[0].values.tolist() )
    sym2 = set( symbol for symbol in df2[0].values.tolist() )
    sym3 = set( symbol for symbol in df3[0].values.tolist() )
    sym4 = set( symbol for symbol in df4[0].values.tolist() )

    # join the 4 sets into one. Because it's a set, there will be no duplicate symbols
    symbols = set.union( sym1, sym2, sym3, sym4 )

    # Some stocks are 5 characters. Those stocks with the suffixes listed below are not of interest.
    my_list = ['W', 'R', 'P', 'Q']
    del_set = set()
    sav_set = set()

    for symbol in symbols:
        if len( symbol ) > 4 and symbol[-1] in my_list:
            del_set.add( symbol )
        else:
            sav_set.add( symbol )
            
    return sav_set


#print(stock_names())
