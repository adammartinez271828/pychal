#!/usr/bin/python
"""
Created on Wed Feb  4 15:22:58 2015

@author: adam
"""

import urllib2
import string

url = 'http://www.pythonchallenge.com/pc/def/ocr.html'

req = urllib2.Request(url)
response = urllib2.urlopen(req)
pagesrc = response.read()

cypher = "!@#$%^&*(){}[]+_<>-\n."

plaintext = pagesrc.translate(None,cypher)

print plaintext