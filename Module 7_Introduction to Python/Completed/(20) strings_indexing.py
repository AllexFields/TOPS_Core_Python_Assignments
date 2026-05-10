#  to get a single string from two given strings,separated by a space and 
# swap the first two characters of each string. 

str1=input("Enter first string: ")
str2=input("Enter second string: ")

final=str1+" " +str2
print(final)

a=str1[:2]+str2[2:]
b=str2[:2]+str1[2:]
print(a,b)
