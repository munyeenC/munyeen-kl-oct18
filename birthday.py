# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 10:42:05 2018

@author: munyeen.chong
"""

import datetime

#birthday = input ("What is your birthday? (dd/mm/YYYY)")

#birthdate = datetime.datetime.strptime(birthday,"%d/%m/%Y").date()

#print ("Your birth month is " + birthdate.strftime('%B'))

nextBirthday = datetime.datetime.strptime('12/20/2019','%m/%d/%Y').date()
currentDate = datetime.date.today()

print (nextBirthday - currentDate)

currentDate = datetime.date.today()

print (currentDate + datetime.timedelta(days=15))
print (currentDate + datetime.timedelta(hours=15))

currDate = datetime.date.today()
print (currDate)
print (currDate.year)
print (currDate.month)
print (currDate.day)

print (currDate.strftime('%A %d %B, %Y'))

print ("Timedelta 15 days : ")
print (currDate = datetime.timedelta(days=15))
print ("Timedelta 15 hours : ")
print (currDate + datetime.timedelta(hours=15))



