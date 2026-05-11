# Python program to get unique values from a list 

lst=[12,98,-12,12,34,25,98]
new_lst=[]

for i in lst:
    if i not in new_lst:
        new_lst.append(i)
for i in new_lst:
    print(i)



# Or we can do this using set ---- set has unique elements

# unique_list=set(lst)
# for i in unique_list:
#     print(i)