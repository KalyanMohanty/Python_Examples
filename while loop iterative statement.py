#while loop
x=1
while x<5:
    print(x)
    x+=1
#find the sum of first n numbers
y=int(input("enter the number:"))
i=1
sum=0
while i<=y:
    sum=sum+i
    print("sum of first",y,"no is:",sum)
    i=i+1

#name and password
name=""
pwd=""
while (name!="kalyan") or (pwd!="kalyan123"):
    print("invalid login")
    name=input("enter the ID:")
    pwd=input("enter password:")
print("Hello there")
#nested loop
for k in range(4):
    for l in range(4):
        print("k={} and l={}".format(k,l))
#infinite loop
#while True:
    #print("hello")

