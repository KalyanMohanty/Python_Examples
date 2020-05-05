s = input("input string:")
a = ''
for ch in s:
    if ch.isalpha():
        x = ch
    else:
        a = a + (x * int(ch))
output = ' '.join(sorted(a))
print(output)
