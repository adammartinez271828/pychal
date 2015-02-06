#!/usr/bin/python
"""
Created on Wed Feb  4 16:25:55 2015

@author: adam
"""

import urllib2
import string

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

#req = urllib2.Request(url + "12345")
#req = urllib2.Request(url + "8022")
req = urllib2.Request(url + "63579")

response = urllib2.urlopen(req)
pagesrc = response.read()

while "next" in pagesrc:
    print url + pagesrc.lstrip(string.letters + string.punctuation + " \n")
    req = urllib2.Request(url + pagesrc.lstrip(string.letters + \
        string.punctuation + " \n"))
    response = urllib2.urlopen(req)
    pagesrc = response.read()
    
print pagesrc