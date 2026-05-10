#  to remove duplicates from a list

lst=[12,15,15,24,-15,12]

emt_lst=[]
for i in lst:
    if i not in emt_lst:
        emt_lst.append(i)

print(f"duplicate values has been deleted\nUpdated list is: {emt_lst}")