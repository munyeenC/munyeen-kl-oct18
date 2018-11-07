# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 10:15:45 2018

@author: munyeen.chong
"""

import csv

myCSVFile = open("data/demo.csv","r")
dataFromFile = csv.reader(myCSVFile)

print(dataFromFile)

for row in dataFromFile:
    print(row)
    
myCSVFile.close()

