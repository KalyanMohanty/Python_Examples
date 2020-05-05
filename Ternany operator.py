#ternary operator
#it is used to when two values are there
#x=first value if condition else second value

#first programme
a,b=10,22
x=30 if (a>20) else 12
print(x)
#second programme
y= 40 if 10>30 else 23
print(y)

#to print minimun number
a=int(input("enter a number:"))
b=int(input("enter a number:"))
min= a if a<b else b
print("minimum number is:",min)

##to print maximum number between 3 inputs
a,b,c=[int(input("enter first number number:")),int(input("enter second number:")),int(input("enter third number:"))]
max=a if a>b and a>c else b if b>c else c
print("maximum number is:",max)

#print equal, greater and small values
l,m=[int(input("enter first number number:")),int(input("enter second number:"))]
max2=l if l>m else m
print("Bigger value is:",max2)
print("Both are equal")
