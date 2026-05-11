# a Python function to check whether a number is in a given range 

# Defining function to check range
def check_range(num,upper_v,lower_v):

    # Checking whether upper limit is smaller than lower limit
    if upper_v<lower_v:
        print("Upper limit must be greater than Lower limit")
        # exit is written here to stop further execution
        exit

    # Checking whether number lies within the given range
    if lower_v<=num<=upper_v:
        print(f"{num} lies in the range {lower_v}:{upper_v}")
    else:
        print(f"{num} doesn't lie in the range {lower_v}:{upper_v}")


num=int(input("Enter number you want to check: "))

upper=int(input("Enter upper limit of range: "))

lower=int(input("Enter lower limit of range: "))

check_range(num,upper,lower)