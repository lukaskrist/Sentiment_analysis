# -*- coding: utf-8 -*-
"""
Created on Mon May 23 18:34:44 2022

@author: loklu
"""
from Stock_simulate import *
from Reddit_data import *
import enchant as ec

names = stock_names()
comments = comment_clean()
names = list(names)

d = ec.Dict("en_US")
for name in names:
    if d.check(name) == True:
        names.remove('name')

i = 0

for comment in comments:
    for com in comment:
        for name in names:
            if str(com).lower() == str(name).lower():
                i += 1
        
        
print(names[0:10])