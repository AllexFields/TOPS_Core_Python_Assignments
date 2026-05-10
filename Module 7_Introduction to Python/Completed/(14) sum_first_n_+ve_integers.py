# sum of first n positive integers

n=int(input("enter value of \"n\": "))
if n>0:
    sum=n*(n+1)//2
    print(f"sum of first {n} positive integers is: {sum}")
else:
    print("Invalid input. Positive integers starts from 1.")