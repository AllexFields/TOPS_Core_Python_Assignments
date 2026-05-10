#  Python program to check whether a list contains a sub list

lst=[12,"astha",34,21,1986,["sushant",11]]
#lst=[13,"shivam",23]

for i in lst:
    if type(i)==list:
        print(f"Given list contains a sub list")
        break
else:
    print(f"Given list doesn't contain a sub list")