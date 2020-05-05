s=input("any string:")
output=''
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1
print(d)
for k,v in sorted(d.items()):
    print('{} occurs {} times'.format(k,v))