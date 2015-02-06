#!/usr/bin/python
"""
Created on Wed Feb  4 14:56:14 2015

@author: adam
"""

cyphertext = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq yp" \
    "c dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq q" \
    "m jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    
# print input_str
    
import string
    
message = string.ascii_lowercase
key = string.ascii_lowercase[2:] + string.ascii_lowercase[0:2]

cypher = string.maketrans(message,key)

print cyphertext.translate(cypher)

cyphertext = "map"

print cyphertext.translate(cypher)
