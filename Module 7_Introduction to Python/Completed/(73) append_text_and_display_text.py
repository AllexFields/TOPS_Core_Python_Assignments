'''a Python program to append text to a file and display the text.

first we created a file "file.txt" and wrote two lines in it.
with open('file.txt','w') as file:
    file.write('this is a file handling question\n')
    file.write('and i need to append a text')

And now we need to append,i.e. add something at the end, a text into this file
and display it'''

# Opening file in append mode
# 'a' mode adds new content at the end of existing file content
with open('file.txt','a') as file:

    # Writing new text into the file    
    file.write('\n\"This is appended text\"')

# Opening file in read mode
# 'r' mode is used to read file content
with open('file.txt','r') as file:    

    # Reading complete file content
    text=file.read()

    # Printing file content
    print(text)