# a Python function to check whether a number is perfect or not.

num=int(input('Enter a number: '))
total=0
product=1
while num!=0:
    digi=num%10
    total+=digi
    product*=digi
    num=num//10
if total==product:
    print(f"{num} is a perfect No")
else:
    print(f"{num} is not a perfect No")