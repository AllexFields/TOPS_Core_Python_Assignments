#  to remove duplicates from a list

lst=[12,15,15,24,-15,12]

# Creating an empty list to store unique elements
emt_lst=[]

for i in lst:
    # Checking whether element already exists in empty list or not
    if i not in emt_lst:
        # Adding unique element into new list
        emt_lst.append(i)         

print(f"duplicate values has been deleted\nUpdated list is: {emt_lst}")