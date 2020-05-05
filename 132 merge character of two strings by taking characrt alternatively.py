s1=input("enter first string").upper()
s2=input("enter second string").lower()
i,j=0,0
output=''
while i<len(s1) or j<len(s2):
    if i<len(s1):
        output = output + s1[i]
        i+=1
    if j<len(s2):
        output = output + s2[i]
        j+=1
print(output)