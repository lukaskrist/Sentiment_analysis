# -*- coding: utf-8 -*-
"""
Created on Mon May 23 18:34:44 2022

@author: loklu
"""
from Stock_simulate import *
from Reddit_data import *


names = stock_names()
comments = comment_clean()
names = list(names)


i = 0
for comment in comments:
    if comment == any(lowercase(names)):
        i += 1
        
print(i)