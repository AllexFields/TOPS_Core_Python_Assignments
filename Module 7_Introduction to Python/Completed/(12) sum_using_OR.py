# if two values are equal then sum is zero

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))

sum=num1+num2+num3

if num1==num2 or num2==num3 or num1==num3:
    print("Sum is 0")
else: print(f"Required sum is {sum}")

