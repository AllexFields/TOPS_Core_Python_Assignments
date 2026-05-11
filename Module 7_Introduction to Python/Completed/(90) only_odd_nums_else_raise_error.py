#  python program that allows user to enter only odd numbers, else 
#  will raise an exception

try:
    # Taking integer input from the user
    user_inp=int(input('Enter an Odd Number: '))

    # Checking whether number is even
    if user_inp%2==0:

        # Raising custom ValueError for even number
        raise ValueError(f"Error: \'{user_inp}\' is an even number. Only odd numbers are allowed")
    
    else:
        # Executing when entered number is odd
        print(f"valid input. {user_inp} is an odd number")
        
except Exception as e:
    print(e)