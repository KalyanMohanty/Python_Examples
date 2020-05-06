# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:58:12 2020

@author: Kalyan Mohanty, COE-AI
"""
'''
openinf files
 syntsax: open('Filename', 'mode')
 mode: r : read ,w: write, a : append
     r+ : read and write
     w+ : write and read
     a+ : append and read
     x : exclusive
=> if mode is not specified 'r is the default mode'
''' 
f = open('test.txt','r')
         # if file is not available the raised error is FileNOtFoundError
f = open('test2.txt','w')
        # if file is available the old data will be over written
        #if not available new file will be created
f = open('test2.txt','a')
        #opns an exiting file
        # overwriting data will not happen
        #data will be append to the file
f= open('test2.txt', 'r+')
        # To read and writw data to file
        #The file pointer is placed at the begining of the file
        #While writing old data will be over written
        # If the specified file is not available the FileNOtFoundError will be raise
f = open('test2.txt','w+')
        # To write and rad data
        # It will over write the existing data
        # If the specied file is not availble then it will create the file
f = open('test2.txt','a+')
        # It won't over write the dat
        # If specied file is not available then this will create the file
f = open('test3.txt','x')
        # Ment for write operation
        #File should not be already available
        # If file already available the FileExistsError will be raised
'''These 7 modes is applicable for text file only'''


print('FileName:',f.name)
print('File Mode:',f.mode)
print('Is File closed:',f.closed)

print('Is file readable:',f.readable()) #returns boolean
print('Is file writable:',f.writable()) #returns boolean
''' Writing data to files
    Syntax = f.write('str')
             f.wtitelines('str')
'''
w = open('write.txt','w')
w.write('kalyan ') 
w.write('Mohanty \n') # Old data will be over written
w = open('write.txt', 'a')
l= ['kalyan ','kumar ','mohanty\n']                               # insted of list we can take tuple, dictonary, set
k = {'kalyan': 100, 'kumar\n': 200}                               # if we pass dictionary only Key will be added and key should be string

m = {'kalyan ', 'kumar ', 'mohanty \n'}                           # In case od set order will not be preserved
w.writelines(l)
w.writelines(k)
#w.writelines(k.values())
w.writelines(m)
                   
w.close()


f.close()



