#  python program that swap two number 

# 1) with temp variable 

x = 2
y = 5

temp=x
x=y
y=temp

print(f"After swapping, x = {x} and y = {y}")



# 2) without temp variable

x = 2
y = 5
x,y = y,x

print(f"After swapping, x = {x} and y = {y}")
