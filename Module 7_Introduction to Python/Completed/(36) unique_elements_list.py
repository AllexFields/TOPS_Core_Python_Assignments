#  a Python function that takes a list and returns a new list with unique elements of the first list

lst=[12,98,-12,12,34,25,98]
new_lst=[]

for i in lst:
    if i not in new_lst:
        new_lst.append(i)
print(f"New list with unique elements is: {new_lst}")