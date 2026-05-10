# a Python function to check whether a number is in a given range 

def check_range(num,upper_v,lower_v):
    if upper_v<lower_v:
        print("Upper limit must be greater than Lower limit")
        exit
    if lower_v<=num<=upper_v:
        print(f"{num} lies in the range {lower_v}:{upper_v}")
    else:
        print(f"{num} doesn't lie in the range {lower_v}:{upper_v}")

num=int(input("Enter number you want to check: "))
upper=int(input("Enter upper limit of range: "))
lower=int(input("Enter lower limit of range: "))

check_range(num,upper,lower)