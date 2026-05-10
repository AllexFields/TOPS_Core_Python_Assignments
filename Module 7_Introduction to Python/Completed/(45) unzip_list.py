# a Python program to unzip a list of tuples into individual lists

a=[(1, 'astha'), (2, 'shivam'), (3, 'vyom'), (4, 'sandeep'), (45, 'anjali')]

lst,lst1=zip(*a)         # *a breaks breaks the tuples into separate arg, and zip makes new tuples from them
# print(type(lst))       # lst and lst1 are two tuples.

print(list(lst),list(lst1))