# a Python program to read an entire text file

# with open('first.txt','w') as file:
#     file.write('Hello there, My name is Shivam Thakur.\n')
#     file.write('This is a file handling question.\n')
#     file.write('I need to read an entire text file.')

# we created a file names 'first.txt' and using w(writing mode), we wrote three lines in it.
# Now we'll read this txt file...

with open('first.txt','r') as file:

    # read prints the entire file
    print(file.read())     