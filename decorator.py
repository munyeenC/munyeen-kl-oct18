# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 10:31:56 2018

@author: munyeen.chong
"""

def say_hello(name):
    return "Hello, " + str(name) + "!"

def p_decorate(func):
    def func_wrapper(name):
        return "<p>" + func(name) + "<p>"
    return func_wrapper

if __name__ == "__main__":
    my_say_hello = p_decorate(say_hello)
     
    print(my_say_hello("John"))