# a python program to find the longest words

# Opening file in read mode
with open('list.txt','r') as f:

    # Reading complete file content
    content=f.read()
    # print(content)

    # split() separates all words and stores them inside a list
    lst=content.split()

    # max() with key=len returns the word having maximum length
    print(f"Longest word in this file is \'{max(lst,key=len)}\'")