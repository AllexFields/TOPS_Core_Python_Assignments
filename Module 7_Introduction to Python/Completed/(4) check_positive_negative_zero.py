#  if a number is positive, negative or zero

user_inp=int(input("Enter a number: "))

if user_inp>0:
    print(f"{user_inp} is positive")
elif user_inp<0:
    print(f"{user_inp} is negative")
else:
    print(f"{user_inp} is zero")