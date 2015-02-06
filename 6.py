#!/usr/bin/python
"""
Created on Wed Feb  4 22:53:02 2015

@author: adam
"""

# import wget
import zipfile
import string

url = "http://www.pythonchallenge.com/pc/def/channel.zip"

# zipped = wget.download(url)

unzipped = zipfile.ZipFile("channel.zip", "r")

nothing = '90052'
nextline = unzipped.read(nothing + '.txt')
comments = ""

while "Next" in nextline:
    nothing = nextline.lstrip(string.letters + ' ')
    nextline = unzipped.read(nothing + '.txt')
    # turns out I need comments too
    comments += unzipped.getinfo(nothing + '.txt').comment

# print nextline

print comments