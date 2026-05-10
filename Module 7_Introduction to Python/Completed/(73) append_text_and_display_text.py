# a Python program to append text to a file and display the text.

# first we created a file "file.txt" and wrote two lines in it.
# with open('file.txt','w') as file:
#     file.write('this is a file handling question\n')
#     file.write('and i need to append a text')

# And now we need to append,i.e. add something at the end, a text into this file
# and display it

with open('file.txt','a') as file:    # 'a' is append mode
    file.write('\n\"This is appended text\"')

with open('file.txt','r') as file:    # 'r' is read mode which will display the text
    text=file.read()
    print(text)