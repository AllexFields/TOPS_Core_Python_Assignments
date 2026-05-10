#  insert a string in the middle of a string

str_1=input("Enter main string: ")
a=str_1[0:len(str_1)//2]
b=str_1[len(str_1)//2:len(str_1)+1]

str_2=input("Enter mid string: ")

ans=a+str_2+b
print(f"Your final string is \"{ans}\"")