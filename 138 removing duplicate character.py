s=input("enter a string:")
output=''
for ch in s:
    if ch not in output:
        output=output+ch
print(output)

#list method
s=input("enter a string:")
l=[]
for ch in s:
    if ch not in l:
        l.append(ch)

print(''.join(l))

#set method
s=input("enter a string:")
s1=set(s)
print(''.join(s1))