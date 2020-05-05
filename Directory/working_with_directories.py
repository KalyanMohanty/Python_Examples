# -*- coding: utf-8 -*-
"""
Created on Tue May  5 14:40:21 2020

@author: Kalyan Mohanty, COE-AI
"""

'''
=============================================================================
To perform different operations in directories we need module'os' 
=============================================================================
'''
#To know current woring directory
import os
cwd = os.getcwd()
print(cwd) 

# To create a directory in current working directory

os.mkdir('Test') # if the dir exists before you will get  FileExistsError
print('Directory created')

#create sub dir in a dir

os.mkdir('Test/Test2')
print('Sub dir created')

#To create both parent and child directory
os.makedirs('t/t1/t2/t3/t4')
print('All dir created')
'''
Q. What is the difference between os.mkdir() and os.makedirs()?
A. os.mkdir() cerates only one directory whereas os.makedirs makes multiple directories.
'''
# To remove a directory
os.rmdir('Test/Test2') #TO remove any directory the directory must be empty; otherwise: OSError 
print('Test2 Directory remved')

os.rmdir('Test') #TO remove any directory the directory must be empty; otherwise: OSError 
print('Test Directory remved')
# To remove a both parent and child directory
os.removedirs('t/t1/t2/t3/t4')
print('All directories are removed')

#TO rename Directory
os.rename('re','rename')
print('Rename completed')

#To know contents of directory
'''
Q. diffrence between os.listdir and os.walk()
A. os.listdir() returns only specified directry files but not sub directory
    whereas os.walk() returns both specified directory and sub directory files 
'''
l = os.listdir('rename') #return type is list
print(l)
l1 = os.walk('rename') #return type is generator object
print(type(l1))
for i in l1:
    print(i)    
    #every element return by generator l1 is a tuple
    #(diectorypath, [dir names],[file names])
    print(type(i))

print()
for dirnames, dirpath, filenames in l1:
    print('Directory path:', dirpath)
    print('Directory name:', dirnames)
    print('File name:', filenames)
    print()

for dirname, _, filenames in os.walk('rename'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
print()
#How to get complete information about a file
'''
st_mode= protection mode, 
st_ino= Inode number,
st_dev= Device, 
st_nlink= Number of hard links,
st_uid= user id of the owner, 
st_gid= group id of the owner, 
st_size= The size of file in bytes, 
st_atime= Time of most recent access, 
st_mtime= Time of most recent modification, 
st_ctime = Time of most recent meta data change

Time return type are in numbers:
    How it is calulated:
      e.g. from 2019 nov 2nd 04:00 PM to 2020 Apr 3rd 05:00 pm 
           The number of mili seconds are calculated as return type.
           We can get datetime module to get exact time
'''    
statistics = os.stat('rename/1.txt')
print(statistics)
print()
from datetime import *
print('file size:', statistics.st_size, 'bytes')
print('Last modified time:', datetime.fromtimestamp(statistics.st_mtime))
