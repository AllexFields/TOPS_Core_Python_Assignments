# a Python script to concatenate following dictionaries to create a new one.

dict_1={"name":'Aastha',"age":21}
dict_2={"city":'Delhi',"hobby":'Cinema'}

'''Manual method to merge dictionaries'''

# merge_dict={}
# for k,v in dict_1.items():
#     merge_dict[k]=v
# for k,v in dict_2.items():
#     merge_dict[k]=v

# Merging dictionaries using union (|) operator
# This operator combines both dictionaries into a new dictionary
merge_dict = dict_1 | dict_2

print(merge_dict)
