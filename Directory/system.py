# -*- coding: utf-8 -*-
"""
Created on Tue May  5 16:34:45 2020

@author: Kalyan Mohanty, COE-AI
"""

'''
OS module contains system() function to run programs and commands.
It is exactly same as system() function in C language,
The aegument can be any valid comand which is executing from DOS.
'''
import os, time
os.system('command') # to open command prompt
os.system('dir')     # to see curent directory
os.system('notepad') # to open notepad
print('Executing test1.py')
os.system('py test1.py')

#time.sleep(7)
#os.system('cls')