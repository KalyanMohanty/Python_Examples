import datetime
import time


def price():
    MRP_HEADPHONE = 400.00
    MRP_MOUSE = 200.00
    MRP_KEYBOARD = 300.00
    MRP_LAPTOP = 50000.00
    MRP_MOUSE_PAD = 100.00


price()

headphone = float(input('Enter the no of headphone customer wants to buy:\t'))
mouse = float(input('Enter the no of mouse customer wants to buy:\t\t'))
keyboard = float(input('Enter the no of keyboard customer wants to buy:\t\t'))
laptop = float(input('Enter the no of laptop customer wants to buy:\t\t'))
mouse_pad = float(input('Enter the no of mouse_pad customer wants to buy:\t'))

print()

print('GENERATING BILL')
time.sleep(3)
print()
print('\tFYLE COMPUTER ASSOCORIES')
print('*' * 45)
currentDT = datetime.datetime.now()
print(str(currentDT))
print()
print('Product\t\t', 'Quantity\t', 'Price')
if headphone > 0:
    h = headphone * MRP_HEADPHONE
    print('Headphone \t', headphone, '\t\t', h)
if mouse > 0:
    m = mouse * MRP_MOUSE
    print('Mouse \t\t', mouse, '\t\t', m)
if keyboard > 0:
    k = keyboard * MRP_KEYBOARD
    print('keyboard \t', keyboard, '\t\t', k)
if laptop > 0:
    l = laptop * MRP_LAPTOP
    print('Laptop \t\t', laptop, '\t\t', l)
if mouse_pad > 0:
    mp = mouse_pad * MRP_MOUSE_PAD
    print('Mouse pad \t', mouse_pad, '\t\t', mp)

tax = (5 * price()) / 100
print(tax)
total = (h + m + k + l + mp)

print()
print('Total \t\t\t\t', total)

