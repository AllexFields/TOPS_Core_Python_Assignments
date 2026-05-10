#  a Python program to get the Fibonacci series of given range

user_input=int(input("Enter range value: "))         # if range = 10, series : 0,1,1,2,3,5,8

a=0
b=1
while a<=user_input:
    print(a,end=" ")
    incr=a+b
    a=b
    b=incr