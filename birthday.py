# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 10:42:05 2018

@author: munyeen.chong
"""

import datetime

#birthday = input ("What is your birthday? (dd/mm/YYYY)")

#birthdate = datetime.datetime.strptime(birthday,"%d/%m/%Y").date()

#print ("Your birth month is " + birthdate.strftime('%B'))

nextBirthday = datetime.datetime.strptime('12/20/2010','%m/%d/%Y').date()
currentDate = datetime.date.today()

print (nextBirthday - currentDate)

