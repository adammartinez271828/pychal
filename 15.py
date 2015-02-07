#!/usr/bin/python
"""
Created on Sat Feb  7 14:02:01 2015

@author: adam
"""

# need to find the year?

# 29 days in Feb -> leap year.

# Year ends in 6

# find date that is a leap year that ends in six where Jan 26 is a Monday

import datetime

for year in range(1996, 1006, -20):
    if datetime.date(year, 1, 26).weekday() == 0:
        print year