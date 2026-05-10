# a python program to find the longest words

with open('list.txt','r') as f:
    content=f.read()
    # print(content)
    lst=content.split()
    print(f"Longest word in this file is \'{max(lst,key=len)}\'")