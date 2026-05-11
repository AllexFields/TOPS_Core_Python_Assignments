# a Python program to convert a list of tuples into a dictionary.

# Creating first list containing keys
lst=[1,2,3,4,45]

# Creating second list containing values
lst1=['astha','shivam','vyom','sandeep','anjali']

# Combining both lists into a list of tuples
# zip() pairs corresponding elements together
a=list(zip(lst,lst1))         


dictionary={}
for i in a:

    # Assigning first tuple element as key
    # and second tuple element as value
    dictionary[i[0]]=i[1]

print(dictionary)