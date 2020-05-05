#RIGHT ANGLE TRINLE
#n=int(input("enter number of rows:"))
#for i in range(n):
   #for j in range(i+1):
    #    print('*',end=' ')
     #   print()

#INVERSE RIGHT ANGLE TRINGLE
n=int(input("enter number of rows:"))
for i in range(n):
    print('* '*(n-i))

#pyramid
n=int(input("enter number of rows:"))
for i in range(n):
    print(" "*(n-i-1)+"^ "*(i+1))
#inverse pyramid
n=int(input("enter number of rows:"))
for i in range(n):
    print(' '*i +"* "*(n-i))

#right half diamond

#diamond
n=int(input("enter number of rows:"))
for i in range(n):
    print(" "*(n-i-1)+"* "*(i+1))
for i in range(n-1):
    print(' '*(i+1)+'* '*(n-i-1))
