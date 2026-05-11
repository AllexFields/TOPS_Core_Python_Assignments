# a Python program to copy the contents of a file to another file

# Opening source file in read mode
with open('list.txt','r') as file:

    # Reading complete content of source file
    content=file.read()

# Opening destination file in write mode
with open('copy.txt','w') as f:

    # Writing copied content into new file
    f.writelines(content)