#split function
#to take multiple inputs
a,b,c=[int(x) for x in input("enter three numbers:").split(',')]
print("the product is:",a*b*c)
print("The sum is :",a+b+c)
if (a*b*c)>(a+b+c):
    print("Double te sum",2*(a+b+c))