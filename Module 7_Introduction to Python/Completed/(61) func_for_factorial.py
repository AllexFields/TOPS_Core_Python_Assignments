# A  Python function to calculate the factorial of a number (a nonnegative integer) 

# Defining function to calculate factorial
def find_factorial(number):

    # Checking whether entered number is negative
    if number<0:
        print("Invalid input. Enter a non-negative integer")
    else:
        # Initializing factorial variable with 1
        factorial=1

        # Loop runs from 1 to entered number (inclusive)
        for i in range(1,number+1):
            # Multiplying factorial with current value of i
            # Same as: factorial = factorial * i
            factorial*=i    
     
        print(f"Factorial of {number} is {factorial}")


user_number=int(input("Enter a number: "))

find_factorial(user_number)