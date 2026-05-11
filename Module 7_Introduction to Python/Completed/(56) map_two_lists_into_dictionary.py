# a Python program to map two lists into a dictionary 
# Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).

# Creating list containing dictionary keys
lst_key=['a','b','c']

# Creating list containing dictionary values
lst_values=[400,400,300]

'''map() applies lambda function on corresponding elements of both lists
lambda x, y: (x, y) creates tuples in key-value pair format
dict() converts those tuples into a dictionary'''

print(dict(map(lambda x,y:(x,y), lst_key,lst_values)))



# Another method:
# zip() combines both lists into tuples
# dict() converts tuples into dictionary

# ans=dict(zip(lst_key,lst_values))
# print(ans)
