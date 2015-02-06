#!/usr/bin/python
"""
Created on Thu Feb  5 15:16:01 2015

@author: adam
"""

# import wget
from PIL import Image
import string

# url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'

# image = wget.download(url)

im = Image.open('oxygen.png')

im = im.crop((0, 45, 608, 46)) #vertical centerline of image, estimated location
    # of data, also crops last 20 pixels on right (junk data)

imdata = im.getdata()

# print list(imdata)

# get first item in list(imdata) tuples and convert to unicode
data = "".join([str(unichr(i[0])) for i in list(imdata)[0::7]])

print data

# convert last bit of ascii
nextlevel = [105, 110, 116, 101, 103, 114, 105, 116, 121]

nextlevel = "".join([str(unichr(i)) for i in nextlevel])

print nextlevel
