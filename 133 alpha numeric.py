s=input("enter first string:")
a=[]
d=[]
for ch in s:
    if ch.isalpha():
        a.append(ch)
    else:
        d.append(ch)
output=(' '.join(sorted(a)+sorted(d)))
print(output)