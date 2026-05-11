#  insert a string in the middle of a string

str_1=input("Enter main string: ")

# Extracting first half of the string
a=str_1[0:len(str_1)//2]

# Extracting second half of the string
b=str_1[len(str_1)//2:len(str_1)+1]

# Taking string to be inserted in the middle
str_2=input("Enter mid string: ")

# Concatenating first half + middle string + second half
ans=a + str_2 + b

print(f"Your final string is \"{ans}\"")