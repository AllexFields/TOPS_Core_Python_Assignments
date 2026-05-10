# a Python script to merge two Python dictionaries 

dict_1={'year':1986,'month':'Jan','day':21}
dict_2={'name':'Gulshan','hobby':'actor','city':'Patna'}

merged_dict={}
for k,v in dict_1.items():
    merged_dict[k]=v
for k,v in dict_2.items():
    merged_dict[k]=v

print(merged_dict)