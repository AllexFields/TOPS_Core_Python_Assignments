# a Python program to count the frequency of words in a file

# Opening file in read mode
with open('first.txt','r') as file:

    # Creating an empty list to store words
    lst=[]

    # Using loop to read file line by line
    while True:

        # readline() reads one line at a time from file
        lines=file.readline()

        # split() separates words based on spaces
        # and stores them inside a list
        r=lines.split()

        # Adding extracted words into lst
        lst+=r

        # If no lines are left, readline() returns empty string
        # This condition stops the loop
        if not lines:
            break
    
    # Creating another list to store already counted words
    lst2=[]

    for i in lst:

        if i not in lst2:
            print(f"{i} ----> {lst.count(i)}")
            
            lst2.append(i)
    