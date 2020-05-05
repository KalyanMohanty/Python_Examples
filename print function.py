#sep
a,b,c=10,20,30
print(a,b,c) #by default space is there
print(a,b,c,sep=',') #sep is used to put other symbols
print(a,b,c,sep=':')
print(a,b,c,sep='|')

# print() with "end" attribute
print("kalyan",end='>')
print("kumar",end=',')
print("mohanty",end='.........')
print("10,20,30",sep=',',end='_________')

#print() "formatted string"
# %d =int type
#%i =int type
#%f =float type
#s =string type
print("a value is: %i \n",a)

#replacement operator {}
name="kalyan mohanty"
salary=100000
friend="sandeep"
print("Hello {} your salary is {} and friend {} is waiting for you".format(name,salary,friend))
print("Hello {z} your salary is {y} and friend {x} is waiting for you".format(z=name,y=salary,x=friend))
print("Hello {0} your salary is {1} and friend {2} is waiting for you".format(name,salary,friend))
