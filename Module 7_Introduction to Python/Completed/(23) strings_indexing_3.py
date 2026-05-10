#Write a Python program to get a string made of the first 2 and the last 2 chars from a given string. 
# If the string length is less than 2, return instead of the empty string.

name=input("Enter a string: ")
if len(name)>=2:
    f_name=name[0:2]
    l_name=name[-2::+1]
    print(f"Ans is {f_name+l_name}")
else:
    print(name)