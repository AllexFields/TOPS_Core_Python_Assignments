# a Python script to sort (ascending and descending) a dictionary by value

dictionary={"name":"Aastha","colour":"blue","city":'delhi'}

sorted_dictionary=dict(sorted(dictionary.items(),key=lambda x:x[1]))
print(sorted_dictionary)