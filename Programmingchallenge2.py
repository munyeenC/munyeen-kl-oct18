# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 11:58:34 2018

@author: munyeen.chong
"""

myFile = open("TestCSV.csv","r")
fileContent = myFile.readline()

while fileContent:
    print(fileContent)
    fileContent = myFile.readline()
    
myFile.close()
