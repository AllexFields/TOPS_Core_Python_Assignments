# A  Python function to calculate the factorial of a number (a nonnegative integer) 

def find_factorial(number):
    if number<0:
        print("Invalid input. Enter a non-negative integer")
    else:
        factorial=1
        for i in range(1,number+1):
            factorial*=i         # same as factorial = factorial*i
        print(f"Factorial of {number} is {factorial}")

user_number=int(input("Enter a number: "))
find_factorial(user_number)