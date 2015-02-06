#!/usr/bin/python
"""
Created on Fri Feb  6 11:19:29 2015

@author: adam
"""

# import binascii

evil2 = open('evil2.gfx', 'r')

# nextline = binascii.hexlify(evil2.readline())

# print nextline

# okay it looks like it's a mashup of five files... FF -- -- -- -- D8 is in 
# there, as well as -- 89 -- -- -- -- 50, which are jpg and png respectively
# need to partition it.  Have to use seek and write to new files

nextchar = evil2.read(1)

file1 = open('file1', 'w+')
file2 = open('file2', 'w+')
file3 = open('file3', 'w+')
file4 = open('file4', 'w+')
file5 = open('file5', 'w+')

while nextchar != "":
    file1.write(nextchar)
    file2.write(evil2.read(1))
    file3.write(evil2.read(1))
    file4.write(evil2.read(1))
    file5.write(evil2.read(1))
    nextchar = evil2.read(1)
    #print nextchar

evil2.close()
