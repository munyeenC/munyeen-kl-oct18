# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 10:25:56 2018

@author: munyeen.chong
"""

def make_inc(x):
    def inc(y):
        #x is closed in the definition of inc
        return x + y
    return inc

if __name__ == "__main__":
    inc5 = make_inc(5)
    inc10 = make_inc(10)
    
    print(inc5(5)) #returns 10
    print(inc10(5)) #returns 15