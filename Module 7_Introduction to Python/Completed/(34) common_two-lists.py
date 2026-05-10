# A Python function that takes two lists and returns true if they have at least one common member

lst1=[23,15,1,12,453]
lst2=['ash','shrine',1,12,21,1986]

for i in lst1:
    if i in lst2:
        print("True")
        break
else:
    print("False")
            
        