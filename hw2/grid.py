# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 09:39:50 2014

@author: bonjun
"""
def do_twice(f):
    f()
    f()
    
def do_fourth(f):
    f()
    f()
    f()
    f()

def print_row():
    print 2*'+ - - - - '+'+'
    
def print_column():
    print 2*'|         '+'|'
    
def print_block():
    print_row()
    do_fourth(print_column)

def print_grid():
    do_twice(print_block)
    print_row()

print_grid()