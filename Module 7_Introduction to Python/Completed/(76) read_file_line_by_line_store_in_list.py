# a Python program to read a file line by line and store it into a list

# Opening file in read mode
with open('first.txt','r') as file:

    # Creating an empty list to store unique lines
    lst_lines=[]

    # Infinite loop to read file line by line
    while True:
        lines=file.readline()

        # If no line is left, readline() returns empty string
        # This condition stops the loop, otherwise loop will run infinitely
        if not lines:
            break
        print(lines)

        # Checking whether line is already present in list or not
        if lines not in lst_lines:
            lst_lines.append(lines)
            
    print(lst_lines)