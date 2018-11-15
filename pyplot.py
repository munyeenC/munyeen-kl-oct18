# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 11:14:38 2018

@author: munyeen.chong
"""

import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.74)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$') #TeX equations
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()