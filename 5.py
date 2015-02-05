# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 16:47:43 2015

@author: adam
"""

import pickle
# import wget

url = "http://www.pythonchallenge.com/pc/def/banner.p"

# banner = wget.download(url)

file = open("banner.p", 'r')

cucumber = pickle.load(file)

str = ""

for i in cucumber:
    for j in i:
        for k in range(j[1]):
            str = str + j[0]
    str = str + "\n"

print str