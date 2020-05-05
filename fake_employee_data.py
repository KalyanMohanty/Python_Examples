from random import *
a='abcdefghijklmnopqrstuvwxyz'
d='12234567890'
city=['Hydrabad','Bhubaneswar','Delhi','Beguluru','Mumbai','Chennai']
designations=['SE','SSE','TL','PL','PM']
def get_fake_name():
    name=choice(a).upper()
    n=randint(2,9)
    for i in range(n):
        name=name+choice(a)
    return name
def get_fake_eno():
    eno='e-'
    for i in range(4):
        eno=eno+choice(d)
    return eno
def get_fake_salary():
    esal=uniform(10000,50000)
    return esal
def get_fake_city():
    citi=choice(city)
    return citi
def get_fake_mobilenumber():
    mno=choice('6789')
    for i in range(9):
        mno=mno+choice(d)
    return mno
def get_fake_designnation():
    des=choice(designations)
    return des
def get_fake_emp_data():
    print("Employee Name:",get_fake_name())
    print('E No:', get_fake_eno())
    print('Salary:{:.2f}'.format(get_fake_salary()))
    print('City Namne:', get_fake_city())
    print('Mobile NO:', get_fake_mobilenumber())
    print('Designnation:', get_fake_designnation())

for i in range(10):
    get_fake_emp_data()
    print()