# a Python program to read last n lines of a file

# Opening file in read mode
with open('first.txt','r') as file:

    # readlines() reads all lines from file
    # and stores them inside a list
    lines=file.readlines()

    # Displaying message to the user
    print("it will give you last n lines")

    # Taking value of n from the user
    last_n_lines=int(input('Enter value for n: '))

    # Using negative slicing to access last n lines
    print(lines[-last_n_lines:])
    