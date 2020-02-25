#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : btc数据处理.py
# Author: MuNian
# Date  : 2020-02-19

import datetime

import pandas as pd
from pandas import Series, DataFrame
from pandas_datareader import data
import matplotlib.pyplot as plt
import matplotlib as mpl


aapl = data.get_data_yahoo('AAPL',
                                 start=datetime.datetime(2019, 10, 1),
                                 end=datetime.datetime(2020, 1, 1))
# print(aapl.head())

aapl.to_csv('data/aapl_ohlc.csv')

df = pd.read_csv('data/aapl_ohlc.csv', index_col='Date', parse_dates=True)
# print(df.head())


close_px = df['Adj Close']
close_px.plot(label='AAPL')
plt.legend()
plt.show()


df = data.get_data_yahoo(['AAPL', 'GE', 'GOOG', 'IBM', 'KO', 'MSFT', 'PEP'],
                               start=datetime.datetime(2015, 1, 1),
                               end=datetime.datetime(2020, 1, 1))['Adj Close']
# print(df.head())


rets = df.pct_change()
plt.scatter(rets.PEP, rets.KO)
plt.xlabel('Returns PEP')
plt.ylabel('Returns KO')
plt.show()

