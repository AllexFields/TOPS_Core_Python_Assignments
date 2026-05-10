# a Python program to convert a list of tuples into a dictionary.

lst=[1,2,3,4,45]
lst1=['astha','shivam','vyom','sandeep','anjali']

a=list(zip(lst,lst1))         # a is a list of tuples

dictionary={}
for i in a:
    dictionary[i[0]]=i[1]

print(dictionary)