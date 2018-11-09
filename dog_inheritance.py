# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 11:51:19 2018

@author: munyeen.chong
"""

class Dog:
    species = "mammal"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

class Bulldog(Dog):
    def run(self, speed)        