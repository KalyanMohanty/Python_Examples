#identity operator (is, is not)
l1=[10,20,30,40,50]
l2=[10,20,30,40,50]
l3=[30,40,50]
l4=[30,40,50]
print(id(l1))
print(id(l2))
print(l1 is l2) #address comparison
print(l1 is not l2)
print(l4 is l1)
print(l3 is not l1)
print(l1==l2)   #address comparision


#membership operator
print(l3 in l1)
print(l2 not in l4)
print(l4 in l3)
print(10 in l1)
print(40 in l1)
