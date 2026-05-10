# a Python program to count the number of lines in a text file.

with open('file.txt','r') as file:
    lines=file.readlines()
    count_no_lines=len(lines)
    print(f"Number of lines in \'file.txt\' = {count_no_lines}")