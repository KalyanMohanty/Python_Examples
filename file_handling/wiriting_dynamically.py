# # -*- coding: utf-8 -*-
# """
# Created on Thu May  7 15:07:59 2020

# @author: Kalyan Mohanty, COE-AI
# """
'''Write data dynamically'''
fname = input('Enter file name:')
f = open(fname,'w')
while True:
    data = input(' Enter data:')
    f.write(data +'\n')
    option = input('Do you want to enter more data: [y/n]')
    if option.lower() == 'n':
        break
print('Data added successfully')
print()
        
f.close()

''' Reading character data from the text file'''
f1 = open('demo.txt','r')
print(f1.read()) # To read all the file
print()
print(f1.read(10)) #To read specified character from the file
'''
===================================================================================
=> f.read(-1) or any minus number will return all the characters from the file

=>\n is also ccounted as one character while counting character. 
space is considered as \n in a text file
===================================================================================
'''
print(f1.read(-123))
print()
# If we will not use end='' then new blank line will present because \n is present at the
#end of every line.
print('First line:',f1.readline(), end = '') # To read line one by one
print('Second line:',f1.readline(), end = '')
print('third line:',f1.readline(), end = '')

#To read all the lines
line = f1.readline()
while line !='':
    print(line, end=' ')
    line = f1.readline()

l = f1.readlines()
for lin in l:
    print(lin, end = ' ')
    
f1.close()
'''
Reading data from one file and write it on another file
'''
f2 = open('demo.txt','r')
f3 = open('demo2.txt','w')
data = f2.read()
print('The data copied Successfully:',f3.write(data))
print('Is file closed:', f2.closed)
f2.close()
f3.close()

''' 
With Statement
=======================================================================================================
* we can use group file operation
* The advantages of with statement is, it will take care of closing of file automatically once control
  reaches end of the with block. Even in case of exception also, file will be closed
  automatically, and not required to close() operation explicitly
=======================================================================================================
'''
with open('demo2.txt', 'r') as f4:
    '''operation is performedd here'''
    f4.read()
    print('Current Crusor position in file:',f4.tell())
    f4.read(4)
    print('Current Crusor position in file:',f4.tell())
    print('Crusor moved to:',f4.seek(3))
print('Is file closed:', f4.closed)


''' tell()  method tells the current crusor postion
    seek(offset, fromwhere) method makes move the croser to a pparticular position
    
    offset indicates number of characters(position) to seek              
    fromwhere allowed values are 0,1 and 2 in python 2.x but in python 3.x only 0 is allowed
                 0- from begining of the file
                 1- from current position
                 2- from end of file
'''


'''How to check a particular file exists or not'''
import os
os.path.isfile('demo2.txt') # returns boolean

#or 
f5 = input('Enter file name:')
if os.path.isfile(f5):
    print('File exists', f5)
    f6 = open(f5,'r')
    text = f6.read()
    print('The content of the file is:', text)
    f6.close()
else:
    print('File does not exist')


