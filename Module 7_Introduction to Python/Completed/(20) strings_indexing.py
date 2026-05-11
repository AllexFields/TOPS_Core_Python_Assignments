#  to get a single string from two given strings,separated by a space and 
# swap the first two characters of each string. 

str1=input("Enter first string: ")
str2=input("Enter second string: ")

# Concatenating both strings with a space in between
final=str1+" " +str2
print(final)

# Creating new string:
# Taking first two characters from str1
# and remaining characters from str2
a=str1[:2]+str2[2:]

# Creating another new string:
# Taking first two characters from str2
# and remaining characters from str1
b=str2[:2]+str1[2:]

# Printing modified string
print(a,b)
