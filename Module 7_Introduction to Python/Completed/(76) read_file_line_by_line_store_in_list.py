# a Python program to read a file line by line and store it into a list

with open('first.txt','r') as file:
    lst_lines=[]
    while True:
        lines=file.readline()
        if not lines:       # it stops the loop when lines end, otherwise readline will execute for infinity
            break
        print(lines)
        if lines not in lst_lines:
            lst_lines.append(lines)
    print(lst_lines)