# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 10:41:28 2018

@author: munyeen.chong
"""

import re

hand = open('data/mbox-short.txt')

for line in hand:
    line = line.rstrip()
#    if line.find('From: ') >= 0:
#        print (line)
#       
    #beginning of the line can have any character
#    if  re.search('From:',line):
#        print(line)
    
    #beginning of the line dont have any character
#    if  re.search('^From:',line):
    
    #if  re.search('^X.*:',line):
    #if  re.search('^X-\S+:',line):
    #    print(line)
    
    #print(re.findall('[0-9]+',line))
    
#    x = 'My 2 favorite numbers are 19 and 42'
#    y = re.findall('[0-9]+',x)
#    print(y)
    
#    x = 'From: Using the : character'
#    y = re.findall('^F.+:',x)
#    print(y)
    
#    if  re.search('[0-9][A-Z]+',line):
#        print(line)    
    
#x = 'From: Using the : character'
#print(re.findall('^F.+',x))  #greedy match  
    
#print(re.findall('^F.+?:',x))   #non-greedy match

#    y = re.findall('\S+@\S+',x)
#    print(y)

    
    
    
    
    
    