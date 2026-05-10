# a Python program to read last n lines of a file

with open('first.txt','r') as file:
    lines=file.readlines()
    print("it will give you last n lines")
    last_n_lines=int(input('Enter value for n: '))
    print(lines[-last_n_lines:])
    