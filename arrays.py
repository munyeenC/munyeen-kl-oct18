# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 11:34:45 2018

@author: munyeen.chong
"""

guests = ['first', 'second','third']
#print(guests[2])

#count from right (the first one)
#print(guests[-1])

#print('First value default :' + guests[0])

guests[0] = 'Steve'
#print('First value is now :' + guests[0])

guests.append('New Guy')

#print('New value is now :' + guests[-1])

#print('2nd Element is :' + guests[1])

#guests.remove('second')
#del guests[1]

#print('2nd Element After remove is :' + guests[1])

#check the index position
#print(guests.index('third'))

#for step in range(len(guests)):
#    print(guests[step])
    
#scores = [78,68,88,98,24]
#print(scores[3])

#count from right (the 2nd one)
#print(scores[-2])

"""
#guests.sort()
#
#for guest in guests:
#    print(guest)
#    
#print("Done")   
"""

scores = [78,68,88,98,24]
scores.sort()
for score in scores:
    print(score)


