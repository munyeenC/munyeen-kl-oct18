# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 09:33:51 2018

@author: munyeen.chong
"""

class Dog:

    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog("doggie1", 1)
dog2 = Dog("doggie2", 2)
dog3 = Dog("doggie3", 3)

def get_biggest_number(*args):
    return max(args)

print("The oldest dog is {} years old.".format(get_biggest_number(dog1.age, dog2.age, dog3.age)))