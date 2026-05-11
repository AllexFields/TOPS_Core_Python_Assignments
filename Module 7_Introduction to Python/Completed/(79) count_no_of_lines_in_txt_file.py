# a Python program to count the number of lines in a text file.

# Opening file in read mode
with open('file.txt','r') as file:

    # readlines() reads all lines from file
    # and stores them inside a list
    lines=file.readlines()

    count_no_lines=len(lines)
    
    print(f"Number of lines in \'file.txt\' = {count_no_lines}")