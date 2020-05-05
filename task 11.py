n = input('INPUT:  ').split(' ')
print(n)
l = list(n)
on = '1'
off = '0'

if len(l) > 1:
    print('OUTPUT :', len(l))
elif len(l)==1 and l[0]=='1':
    print('OUTPUT :', '0')
elif len(l)==1 and l[0]=='0':
    print('OUTPUT : ','1')
