# a Python program to map two lists into a dictionary 
# Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).

lst_key=['a','b','c']
lst_values=[400,400,300]

print(dict(map(lambda x,y:(x,y), lst_key,lst_values)))

# Or we can use zip and then convert it into dictionary

# ans=dict(zip(lst_key,lst_values))
# print(ans)
