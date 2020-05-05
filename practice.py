# n=int(input('Enter the No.:'))
import time
n = 8
def tringle():
    for i in range(n):
        print(i * '*')
tringle()
#time.sleep(1)
def reverse_tringle():
    for i in range(n):
        print((n - i) * '*')
reverse_tringle()
#time.sleep(1)
def pyramid():
    for i in range(n):
        print(' ' * (n - i), '*' + i * '*' + i * '*' + ' ' * (n - i))
pyramid()
#time.sleep(1)
def straight_line():
    for i in range(n):
        print(' ' * 7, 3 * '*')
straight_line()
#time.sleep(1)
def invert_pyramid():
    for i in range(n):
        print(' ' * i, '*' * (n - i) + '*' * (n - i))
invert_pyramid()

def roof():
    for i in range(7):
        print(' '*(7-i),'*'+i*'*'+('*'*65)+ i* '*')
roof()
def wall():
    print(' ' * 7, '*' *65)
    print(' ' * 7, '*' * 65)
    for i in range(7):
        print(' '*7,'*'*13,' '*10,'*'*15, ' '*10, '*'*13)
    print('*' * 85)
    print('*' * 85)
wall()
def road():
    for i in range(25):
        print(' '*(25-i),'*')
road()