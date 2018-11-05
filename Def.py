# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 11:00:08 2018

@author: munyeen.chong
"""
"""
#1. create a function to print hello
def sayHello(firstName, lastName) :
    print("Hello " + firstName + " " + lastName + ", how are you?")
    return

#2. invoke the function
sayHello("Shirley"," ")

sayHello("Charlie"," Test")

sayHello("Everyone"," ")

def addTwo(var1,var2) :
    sum = var1 + var2
    return sum

print("Sum of 5 + 5 = " + str(addTwo(5,5)))
"""
def printinfo( name, age = 16, location="KL" ):
    "This prints a passed info into this function"
    print ("Name: ", name)
    print ("Age ", age)
    print ("Location ", location)
    return;

printinfo("miki",50,"Penang")  
printinfo("miki",50)    
printinfo(age=50, name="miki",location="PJ")    
printinfo( name="mini")   
    
    