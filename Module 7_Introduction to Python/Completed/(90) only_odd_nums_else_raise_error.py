#  python program that allows user to enter only odd numbers, else 
#  will raise an exception

try:
    user_inp=int(input('Enter an Odd Number: '))
    if user_inp%2==0:
        raise ValueError(f"Error: \'{user_inp}\' is an even number. Only odd numbers are allowed")
    else:
        print(f"valid input. {user_inp} is an odd number")
except Exception as e:
    print(e)