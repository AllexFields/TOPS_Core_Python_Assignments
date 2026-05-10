# a Python program to count the frequency of words in a file

with open('first.txt','r') as file:
    lst=[]
# using a loop to read file line-by-line until there's no line to read

    while True:
        lines=file.readline()  #readline reads the file line-by-line,i.e. one line at a time
        r=lines.split()        #split method --- by default it creates a list by splitting a string separated by spaces
        lst+=r
        if not lines:
            break
        # print(lines)
    # print(lst)
    
    lst2=[]
    for i in lst:
        if i not in lst2:
            print(f"{i} ----> {lst.count(i)}")
            lst2.append(i)
    