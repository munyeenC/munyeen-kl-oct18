# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import datetime

currDate = datetime.date.today()
print (currDate)
print (currDate.year)
print (currDate.month)
print (currDate.day)

#print (currDate.strftime('%d %b, %y'))

print (currDate.strftime('%d %b, %Y'))

print (currDate.strftime('Please attend our event %A %d %B, %Y'))



