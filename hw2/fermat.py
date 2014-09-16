# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 10:00:33 2014

@author: bonjun
"""

def check_fermat(a,b,c,n):
    if(a**n+b**n==c**n):
        print "Holy smokes, Fermat was wrong!"
    else:
        print "No, that doesn't work."

def ask():
     a = raw_input("a = ?\n")
     b = raw_input("b = ?\n")
     c = raw_input("c = ?\n")
     n = raw_input("n = ?\n")
     check_fermat(int(a),int(b),int(c),int(n))

ask()