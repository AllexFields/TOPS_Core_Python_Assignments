#  true if the two given integer values are equal or their sum or difference is 5

integer_1=int(input("Enter first integer: "))
integer_2=int(input("Enter second integer: "))

sum=integer_1+integer_2
difference=abs(integer_1-integer_2)

if integer_1==integer_2 or sum==5 or difference==5:
    print("True")
else: print("False")
