s=input("input string:")
l=s.split()
i=0
l1=[]
while i<len(l):
    if i%2==0:
        l1.append(l[i])
    else:
        l1.append(l[i][::-1])
    i=i+1
print(' '.join(l1))
