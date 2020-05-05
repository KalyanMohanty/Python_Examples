# -*- coding: utf-8 -*-
"""
Created on Mon May  4 14:17:34 2020

@author: Kalyan Mohanty
"""

'''
===============================================================
1. saves memory
2. transportation time reduces
3. it is very convenient to use
4. We can improve the performance

To perform zip an d unzip files in python 
module: zipfile
class: ZipFile
==============================================================
''' 
#Zipping

from zipfile import *
f = ZipFile('files.zip', 'w', ZIP_DEFLATED)
'''first we have to create zip file object
 ZIP_DEFLATED is used to zip the files whereas 
 ZIP_STORED is usedto unzip the file 
'''
f.write('test1.txt')
#f.write('csv.py')
f.write('test2.txt')

#Unzipping 
f = ZipFile('files.zip', 'r', ZIP_STORED)
names = f.namelist()
print(names)
for name in names:
    f1 = open(name,'r')
    text = f1.read()
    print('file name:', name)
    print('content of this file:')
    print(text)
    f.close()
    print()
