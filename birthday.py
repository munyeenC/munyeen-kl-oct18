# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 10:42:05 2018

@author: munyeen.chong
"""

import datetime

birthday = input ("What is your birthday? ")

birthdate = datetime.datetime.strptime(birthday,"%d/%m/%Y").date()

print ("Your birth month is " + birthdate.strftime('%B'))


