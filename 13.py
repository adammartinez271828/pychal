#!/usr/bin/python
"""
Created on Sat Feb  7 12:02:44 2015

@author: adam
"""

# It turns out this one is xml-rpc, which I know nothing about.  Had to look 
# up a hint.

import xmlrpclib

url = 'http://www.pythonchallenge.com/pc/phonebook.php'

server = xmlrpclib.Server(url)

# Okay, have access... need to figure out what to do from here

for method in server.system.listMethods():
    print method
    print server.system.methodHelp(method)
    
# Phone looks interesting.  From the last problem, Bert was evil...
    
server.phone('Bert')
