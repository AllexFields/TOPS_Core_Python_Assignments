# a Python program to read first n lines of a file

no_of_lines=int(input('Only first n lines will be printed\nEnter how many lines you want to read: '))
with open('first.txt','r') as file:
    for i in range(no_of_lines):
        print(file.readline())