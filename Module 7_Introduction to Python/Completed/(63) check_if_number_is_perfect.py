# a Python function to check whether a number is perfect or not.

num=int(input('Enter a number: '))

# Storing original number for final display
original_num = num

# Initializing variables
total=0
product=1

# Loop runs until number becomes 0
while num!=0:
    # Extracting last digit of number
    digi=num%10

    # Adding digit into total
    total+=digi

    # Multiplying digit into product
    product*=digi

    # Removing last digit from number
    num=num//10
   
if total==product:
    print(f"{num} is a perfect No")
    
else:
    print(f"{num} is not a perfect No")