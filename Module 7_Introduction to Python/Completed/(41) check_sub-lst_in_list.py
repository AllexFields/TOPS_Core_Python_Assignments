#  Python program to check whether a list contains a sub list


# Creating a list that may contain another list inside it
lst=[12,"astha",34,21,1986,["sushant",11]]

for i in lst:

    # Checking whether current element is of list type or not
    if type(i)==list:
        print(f"Given list contains a sub list")

        # Exiting loop immediately after finding first sub list
        break

# This else block belongs to the for loop, not to the if statement
# It executes only when the loop completes normally
# without encountering a break statement
else:
    print(f"Given list doesn't contain a sub list")