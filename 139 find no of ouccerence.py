s=input("enter a string:")
l=[]
for ch in s:
   if ch not in l:
       l.append(ch)
print(l)
for ch in sorted(l):
    print('{} occurs {} times'.format(ch,s.count(ch)))