s=input("enter string:")
output=''
for ch in s:
    if ch.isalpha():
        output=output+ch
        x=ch
    else:
        d=int(ch)
        newch=chr(ord(ch)+d)
        output=output+newch
print(output)
