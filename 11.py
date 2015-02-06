#!/usr/bin/python
"""
Created on Fri Feb  6 10:26:09 2015

@author: adam
"""

import Image

im = Image.open('cave.jpg')

# page name is odd-even...  looks like a composite of two images... perhaps
# even-odd columns?  rows? ... gimp says checkerboard

# get direct access to pixel level manipulation
pix = im.load()

# blank out all even pixels on odd rows
for x in range(1, im.size[0], 2):
    for y in range(0, im.size[1], 2):
        pix[x,y] = (0,0,0)
        
# blank out all odd pixels on even rows
for x in range(0, im.size[0], 2):
    for y in range(1, im.size[1], 2):
        pix[x,y] = (0,0,0)

im.save('even.jpg')