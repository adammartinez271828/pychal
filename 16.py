#!/usr/bin/python
"""
Created on Sat Feb  7 14:15:08 2015

@author: adam
"""

# align the pink bars

import Image

im = Image.open('mozart.png')

pix = im.load()

for r in range(im.size[1]):
    # let's push them to the right