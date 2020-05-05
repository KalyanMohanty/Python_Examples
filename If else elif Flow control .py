# conditional statement
brand=input("please enter the brand:")
if brand=="fasttrack":
    print("Good for sunglsses")
elif brand=="adidas":
    print("Good for t-shirt")
elif brand=="nike":
    print("Good for Shoes")
else:
    print("Other brands are not Good")
#to check number
n=int(input("enter any number:"))
if 1<n<100:
    print("The number",n,"is in between 1 and 100")
else:
    print("the number",n,"Not available in between 1 and 100")