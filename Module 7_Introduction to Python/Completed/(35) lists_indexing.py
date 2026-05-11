# A Python program to generate and print a list of first and last 5 elements 
# where the values are square of numbers between 1 and 30

Lst_squares=[]

# Loop runs from 1 to 30 (31 is excluded)
for i in range(1,31):
    squares=i*i
    
    # add squares of each no in the list
    Lst_squares.append(squares)

print(f"First 5 elements: {Lst_squares[0:5]}")

print(f"Last 5 elements: {Lst_squares[25:30]}")

