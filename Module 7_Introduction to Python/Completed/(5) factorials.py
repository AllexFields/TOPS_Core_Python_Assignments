#  a Python program to get the Factorial number of given numbers

user_inp=int(input("Enter a number: "))

factorial=1
for i in range(1,user_inp+1):         # the loop always runs one time lesser than our 'end' parameter
    factorial*=i
print(f"factorial of {user_inp} is {factorial}")