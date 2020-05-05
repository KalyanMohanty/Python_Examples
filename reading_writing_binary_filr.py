# -*- coding: utf-8 -*-
"""
Created on Mon May  4 14:04:23 2020

@author: Kalyan Mohanty
"""

f1 = open('data1.jpg', 'rb')
data = f1.read()
f2 = open('data2.jpg', 'wb')
f2.write(data)
print('data is ready')