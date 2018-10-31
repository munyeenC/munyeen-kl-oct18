# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 11:07:47 2018

@author: munyeen.chong
"""

import datetime

currentTime = datetime.datetime.now()

print (currentTime)
print (currentTime.hour)
print (currentTime.minute)
print (currentTime.second)

print (datetime.datetime.strftime(currentTime,'%H:%M'))

print (datetime.datetime.strftime(currentTime,'%I:%M %p'))

