# Add 'in' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead.
# if the string length of the given string is less than 3, leave it unchanged.

name=input("Enter a string: ")

# Storing original string into another variable
ans=name

# Checking if length of string is greater than or equal to 3
if len(name)>=3:

    # Checking whether string ends with "ing"
    if name[-3:]=="ing":
        name=name+"ly"
        print(f"Answer is: {name}")
    else:
        ans=ans+"in"
        print(f"Answer is: {ans}")
else:
    print(f"Answer is: {ans}")

