s=input("input string:")
output=s.split()
r=' '.join(reversed(output))
print(r)

#slice operator
s=input("input string:")
s1=s.split()
output=s1[::-1]
l=' '.join(output)
print("output:",l)