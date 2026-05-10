# a Python program to read a file line by line and store it into a variable

with open('file.txt','r') as f:
    string=""
    while True:
        lines=f.readline()
        if not lines:       # it stops the loop when lines end, otherwise readline will execute for infinity
            break
        print(lines)
        string+="----> "+lines+'\t'    # concatenated each line into empty string
        
    print(f"the content of file.txt is stored inside a string as following:-\n\t{string}")