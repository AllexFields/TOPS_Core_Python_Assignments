#  a Python function that takes a list and returns a new list with unique elements of the first list

lst=[12,98,-12,12,34,25,98]
new_lst=[]

# Traverse through every element of lst
for i in lst:

    # Checking whether element already exists in empty list or not
    if i not in new_lst:

        # Adding unique element into new list
        new_lst.append(i)
        
print(f"New list with unique elements is: {new_lst}")