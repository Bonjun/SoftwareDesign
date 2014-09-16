# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 10:22:49 2014

@author: bonjun
"""

def compare():
    x=raw_input("X = ?")
    y=raw_input("Y = ?")
    if int(x)>int(y):
        return 1
    if int(x)==int(y):
        return 0
    if int(x)<int(y): 
        return -1


compare()