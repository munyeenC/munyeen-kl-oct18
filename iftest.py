# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 11:18:15 2018

@author: munyeen.chong
"""

#shippingSelected = False
answer=input("Would you like express shipping? (Yes or No)").lower()

if answer == "yes" :
    print ("That will be an extra $10")
    shippingSelected = True
else:
    print("Standard Shipping selected..")
    
print("Thank you")

if(shippingSelected) :
    print("Thank you for selecting the shipping options!!")

#######################################    
#deposit = input("How much would you like to deposit? ")
#if float(deposit) > 100 :
#    print("You get a free toaster!")
#else:
#    print("Enjoy your mug!")
#print("Have a nice day")

#freeToaster=False
#deposit = input("How much would you like to deposit? ")
#if float(deposit) > 100 :
#    freeToaster=True
    
#if freeToaster :
#    print("enjoy your toaster")
    

        


    