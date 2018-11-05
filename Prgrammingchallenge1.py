# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:29:16 2018

@author: munyeen.chong
"""

#answer = 0
#
#while answer != " ":
#    answer = int(input("What is your name? "))
#    
#print("Yes! 2+2 = 4")  
#

Participants = []
Participant = 0

while Participant != " ":
    Participant = input("What is your name? ")
    Participants.append(Participant)
    
Participants.sort()

for Participant in Participants:
    print(Participant)
    
    
    

 