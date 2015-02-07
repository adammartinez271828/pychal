#!/usr/bin/python
"""
Created on Sat Feb  7 12:10:47 2015

@author: adam
"""

# There's a bun and a small file called wire.  Walk around in a circle like
# the bun? actually no, coil the wire back up that way.

import Image

wire = Image.open('wire.png', 'r')
coil = Image.new('RGB', (100,100), 'white')

# get direct access to pixel level manipulation
wirepix = list(wire.getdata())
coilpix = coil.load()

# what we can do is shrink our working area as we go around
# for an mxm square, we can put four m-1 wires on all four sides and then do
# a smaller square inside.
tl = 0
br = 99

def wrap(wire, coil, tl, br):
    # wrap around exterior starting with upper left corner
    # find wire length needed for each edge
    wirelength = br-tl
    # print wirelength
    
    if wirelength > 0:
    
        # wrap top
        for i in range(wirelength):
            coilpix[tl+i, tl] = wirepix.pop()
            print (tl+i, tl)
        # wrap right
        for i in range(wirelength):
            coilpix[br, tl+i] = wirepix.pop()
            print (br, tl+i)
        # wrap bottom
        for i in range(wirelength):
            coilpix[br-i, br] = wirepix.pop()
            print (br-i, br)
        # wrap left
        for i in range(wirelength):
            coilpix[tl, br-i] = wirepix.pop()        
            print (tl, br-i)
            
        # recursively call on interior
        wrap(wire, coil, tl+1, br-1)    
        return None

    # if wirelength = 0, we are done: note this will not handle rectangles 
    # with odd edge lengths

wrap(wirepix, coilpix, tl, br)

coil.save('coil.bmp')

coil.show()

