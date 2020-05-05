#calculate simple interest
p=int(input("please enter your principal amount:"))
t=int(input("please enter the duration of interest:"))
r=eval(input("please enter the rate of interest:"))
SI=(p*t*r)/100
print("The simple interest is :", SI)
print("Total amount to be paid is:", SI+p)
