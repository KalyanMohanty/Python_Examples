n=int(input('enter the number of students:'))
d={}
for i in range(n):
    name=input("enter the name of student:")
    mark=int(input('enter the mark:'))
    d[name]=mark
print('student data insertion s completed')
print('*'*30)
print('name','\t\t','marks')
print('*'*30)
for k,v in d.items():
    print(k,'\t\t',v)
print('search operation started...')
while True:
    name=input('enter the student name to get thee mark')
    mark=d.get(name,-1)
    if mark==-1:
        print('student not found')
    else:
        print('mark of the',name,'is',mark)
    option=input('search for another student y/n:')
    if option.lower()==n:
        break
print('Thanks for using our application !!!')