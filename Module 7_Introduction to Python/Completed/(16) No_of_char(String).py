# No. of characters in a string

name=input("Enter any string: ")
lst=[]
count=0
for i in name:
    if i not in lst:
        count+=1
        print(f"{i} ---> {name.count(i)} ")
        lst.append(i)
print(f"No of characters in \"{name}\" is {len(name)}")