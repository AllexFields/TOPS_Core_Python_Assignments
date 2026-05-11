# a Python program to read a file line by line and store it into a variable

# Opening file in read mode
with open('file.txt','r') as f:
    
    string=""

    while True:
        lines=f.readline()

        # If no lines are left, readline() returns empty string
        # This condition stops the loop, otherwise loop will run infinitely
        if not lines:
            break
        print(lines)

        # Concatenating each line into the string
        # '\t' adds tab spacing
        string+="----> "+lines+'\t'   
        
    print(f"the content of file.txt is stored inside a string as following:-\n\t{string}")