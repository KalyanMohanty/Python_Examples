# Write a Python program to print all even numbers from a given numbers list
# in the same order and stop the printing if any numbers that come after 237 in the sequence.
n=[100,200,23,345,232,222,456,677,678,568,34,13,79,556,7678,67768,656789]
for i in n:
    if (i>30) and (i%2==0):
        print("even numbers are:",i)

