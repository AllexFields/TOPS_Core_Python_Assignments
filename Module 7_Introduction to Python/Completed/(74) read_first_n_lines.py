# a Python program to read first n lines of a file

# Taking number of lines input from the user
no_of_lines=int(input('Only first n lines will be printed\nEnter how many lines you want to read: '))

# Opening file in read mode
with open('first.txt','r') as file:

    # Loop runs according to number of lines entered by user
    for i in range(no_of_lines):

        # readline() reads one line at a time from the file
        print(file.readline())