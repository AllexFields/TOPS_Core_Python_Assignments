# a Python script to sort (ascending and descending) a dictionary by value

dictionary={"name":"Aastha","colour":"blue","city":'delhi'}

'''Sorting dictionary items based on values
dictionary.items() returns key-value pairs as tuples
lambda x: x[1] means sorting will happen using tuple's second element (value)'''

sorted_dictionary=dict(sorted(dictionary.items(),key=lambda x:x[1]))


print(sorted_dictionary)