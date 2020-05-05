s=input("input string:")
l=s.split()
l1=[]
for word in l:
    l1.append(word[::-1])
print(' '.join(l1))
