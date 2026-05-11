#  a Python program to get the Factorial number of given numbers

# Taking input from the user
user_inp=int(input("Enter a number: "))

# Initializing factorial variable with 1
factorial=1

# Loop runs from 1 to user_inp (inclusive)
# range() excludes the ending value, so we use user_inp + 1
for i in range(1,user_inp+1):         
    factorial*=i
    
print(f"factorial of {user_inp} is {factorial}")