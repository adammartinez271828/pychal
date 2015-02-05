# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 22:53:02 2015

@author: adam
"""

import wget

url = "http://www.pythonchallenge.com/pc/def/channel.jpg"

banner = wget.download(url)

file = open("banner.p", 'r')