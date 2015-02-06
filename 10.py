#!/usr/bin/python
"""
Created on Fri Feb  6 09:55:27 2015

@author: adam
"""

# hint is len(a(30))?  Obvously have to find the length of the 30th element of
# the sequence in the image hint: a = [1, 11, 21, 1211, 111221, 

# it's a see-and-say sequence... need an easy way to generate new elements

a = [1]

def cnsay(arg):
    # accepts integer argument and spits out a see-and-say expansion of it
    # lstrip seems like the best idea here - typecast as string
    expansion = ""
    arg = str(arg)
    while len(arg) > 0:
        expansion += str(len(arg) - len(arg.lstrip(arg[0]))) + arg[0]
        arg = arg.lstrip(arg[0])
    
    return int(expansion)
    
for i in range(0,30):
    a.append(cnsay(a[i]))
    
print len(str(a[30]))
