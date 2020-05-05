s = input("input string:")
previous = s[0]
output=''
count = 1
i = 1
while i<len(s):
    if s[i] == previous:
        count += 1
    else:
        output=output+str(count)+previous
        previous=s[i]
        count=1
    if i==len(s)-1:
        output=output+str(count)+previous
        i=i+1
print(output)
