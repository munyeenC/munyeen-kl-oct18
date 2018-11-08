# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 10:29:03 2018

@author: munyeen.chong
"""
"""
class Puppy:
    name = ""
    color = ""
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def bark(self):
        print("I am", self.color, self.name)
        
puppy1 = Puppy("Max","brown")    
puppy1.bark()

puppy2 = Puppy("Ruby","black")
puppy2.bark()
"""

class Critter:
    name = ""
    
    def __init__(self, name):
        self.name = name
        
    def talk(self):
        print("Hi. I am", self.name)
        
crit = Critter("AAA")        
crit.talk()