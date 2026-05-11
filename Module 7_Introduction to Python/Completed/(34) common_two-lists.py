# A Python function that takes two lists and returns true if they have at least one common member

lst1=[23,15,1,12,453]
lst2=['ash','shrine',1,12,21,1986]

# Traversing through each element of first list
for i in lst1:

    # Checking whether current element exists in second list
    if i in lst2:
        print("True")

        # Exiting loop after finding first common member
        break

# This else block executes only if loop completes normally
# without encountering break statement
else:
    print("False")
            
        