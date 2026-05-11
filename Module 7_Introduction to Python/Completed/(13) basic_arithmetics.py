# Program to check the following conditions:
# 1. If both integers are equal
# 2. If their sum is 5
# 3. If their absolute difference is 5


integer_1=int(input("Enter first integer: "))
integer_2=int(input("Enter second integer: "))

# abs() converts negative values into positive values
sum=integer_1+integer_2
difference=abs(integer_1-integer_2)

if integer_1==integer_2 or sum==5 or difference==5:
    print("True")
    
else: print("False")
