# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 11:26:23 2018

@author: munyeen.chong
"""
counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1

print(counts)     

print(counts.get("csev",0))

print(counts.get('aaa',0))