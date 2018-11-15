# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 10:12:53 2018

@author: munyeen.chong
"""

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
    
try:
    raise MyError(2*2)
except MyError as e:
    print("My exception occured, value", e)    