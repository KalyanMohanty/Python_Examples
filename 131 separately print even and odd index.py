s=input("input string:")
i=0
print("the chharacters are present at even index are:")
while i<len(s):
    print(s[i])
    i+=2
i=1
print("the chharacters are present at odd index are:")
while i<len(s):
    print(s[i])
    i+=2

l1=s[0::2]
print("the chharacters are present at even index are:",l1)

l1=s[1::2]
print("the chharacters are present at odd index are:",l1)