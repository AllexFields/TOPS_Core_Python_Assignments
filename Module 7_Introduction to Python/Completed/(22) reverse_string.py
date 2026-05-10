#  to reverses a string if its length is a multiple of 4.

name=input("Enter a string: ")
if len(name)%4==0:
    print(f"Answer is --- {name[-1::-1]}")
else:
    print(f"Invalid input --- length of the string should be a multiple of 4")