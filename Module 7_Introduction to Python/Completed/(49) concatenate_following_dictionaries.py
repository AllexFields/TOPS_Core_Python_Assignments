# a Python script to concatenate following dictionaries to create a new one.

dict_1={"name":'Aastha',"age":21}
dict_2={"city":'Delhi',"hobby":'Cinema'}

merge_dict={}
for k,v in dict_1.items():
    merge_dict[k]=v
for k,v in dict_2.items():
    merge_dict[k]=v

print(merge_dict)
