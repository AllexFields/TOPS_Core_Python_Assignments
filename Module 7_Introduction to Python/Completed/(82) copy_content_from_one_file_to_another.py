# a Python program to copy the contents of a file to another file

with open('list.txt','r') as file:
    content=file.read()
with open('copy.txt','w') as f:
    f.writelines(content)