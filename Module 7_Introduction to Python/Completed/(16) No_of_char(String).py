# No. of characters in a string

name=input("Enter any string: ")

# Creating an empty list to store already checked characters
lst=[]
count=0

# Traversing through each character of the string
for i in name:

    # Checking whether character is already counted or not
    if i not in lst:

        # Increasing count for unique characters
        count+=1
        print(f"{i} ---> {name.count(i)} ")

        # Adding counted character into list
        lst.append(i)
        
print(f"No of characters in \"{name}\" is {len(name)}")