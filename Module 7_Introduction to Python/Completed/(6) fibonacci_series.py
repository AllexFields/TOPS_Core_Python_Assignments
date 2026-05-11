#  a Python program to get the Fibonacci series of given range

# Taking range value input from the user
# Example: if input = 10, output will be: 0 1 1 2 3 5 8
user_input=int(input("Enter range value: "))         

# Initializing first two Fibonacci numbers
a=0
b=1

while a<=user_input:

    # Printing current Fibonacci number
    print(a,end=" ")

    # Calculating next Fibonacci number
    incr=a+b

    # Updating values for next iteration
    a=b
    b=incr