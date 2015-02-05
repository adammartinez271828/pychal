# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 15:22:58 2015

@author: adam
"""

import urllib2
import re

url = 'http://www.pythonchallenge.com/pc/def/equality.html'

req = urllib2.Request(url)
response = urllib2.urlopen(req)
pagesrc = response.read()

# print pagesrc

solution = ""

x = re.findall('[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]', pagesrc)

print x

for i,j in enumerate(x):
    x[i] = j[4:5]
    
print x    
    
print solution.join(x)