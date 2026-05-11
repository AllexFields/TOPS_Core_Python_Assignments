#  if a number is positive, negative or zero

# Taking input from the user and converting it into integer
user_inp=int(input("Enter a number: "))

# Checking if the number is greater than 0
if user_inp>0:
    print(f"{user_inp} is positive")

# Checking if the number is less than 0
elif user_inp<0:
    print(f"{user_inp} is negative")

# If the number is neither positive nor negative, then it is zero
else:
    print(f"{user_inp} is zero")