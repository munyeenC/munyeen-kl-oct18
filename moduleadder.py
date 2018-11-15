# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 10:36:34 2018

@author: munyeen.chong
"""

#def add_item(item, item_list = []):
#    item_list.append(item)
#    print(item_list)

def add_item(item, item_list = None):
   if item_list == None:
       item_list = []
   item_list.append(item)
   print(item_list)
   

def printDict(**kwargs):
    print(kwargs)
    
def printTuple(*args):
    print(args)    
    