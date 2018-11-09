# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 10:29:03 2018

@author: munyeen.chong
"""

class Puppy:
    name = ""
    color = ""
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def bark(self):
        print("I am", self.color, self.name)
        
    def __str__(self):
        ret = "Puppy Object\n"
        ret += "name:" + self.name + "\n"
        return ret        
        
puppy1 = Puppy("Max","brown")    
puppy1.bark()

puppy2 = Puppy("Ruby","black")
puppy2.bark()

#will have error as we did not put in the name and color (max and brown)
#puppy3 = Puppy() 
#puppy3.bark()

#print (puppy2.name)

#print (dir(puppy2))

#print ("Puppy2 is :" + puppy2)
print (puppy2)
"""
class Critter:
    name = ""
    
    def __init__(self, name):
        self.name = name
        
    def talk(self):
        print("Hi. I am", self.name)
        
crit = Critter("AAA")        
crit.talk()
"""
"""
class Test:
    
    def talk(self, msg):
        print(msg)
        
    def myName(self):
        print("I am Test...")
        
obj1 = Test()
obj1.talk("Hi")
obj1.myName()   

obj2 = Test("Hi")
obj2.myName()     
"""        
        