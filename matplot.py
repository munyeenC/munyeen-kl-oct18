# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 11:07:58 2018

@author: munyeen.chong
"""

import matplotlib.pyplot as plt

plt.plot([1,2,3,4,5])
plt.ylabel('Some significant numbers')
plt.show()

#integrated with Numpy
import numpy as np

t = np.arange(1.,5.,0.2)

plt.plot(t,t,'r--',t,t**2,'gs',t,t**3,'y^')
plt.axis([0,6,0,150]) #x and y axis range
plt.show()
