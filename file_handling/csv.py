# -*- coding: utf-8 -*-
"""
Created on Mon May  4 13:22:58 2020

@author: Kalyan Mohanty
"""
'''
=====================================================
wirting csv file by using pythons inbuilt csv module
=====================================================
'''

with open('demo.csv', 'w') as f: # 'w' mode will create an new csv file if there is not an exiting csv file
    w = csv.writer(f)
    w.writerow(['e_no','e_name', 'e_address','e_mob'1])
    while True:
        e_no = int(input('enter e no:' ))
        e_name = input('enter e name:')
        e_address = input('enter e address:')
        e_mob = int(input('enter e mobile no:'))
        option = input('Do you want to ontinue: [y/n]')
        w.writerow([e_no,e_name, e_address,e_mob])
        if option.lower()== 'n':
            break
print('employee data written to CSV file')

'''
====================================================
Reading csv file by using pythons inbuilt csv module
====================================================
'''

with open('demo.csv','r') as f:
    r = csv.reader(f)
    data = list(r)
    #print(data)
    for row in data:
        for column in row:
            print(column ,'\t', end = '' )
        