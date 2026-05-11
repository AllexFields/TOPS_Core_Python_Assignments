# a Python program to write a list to a file

# Creating a list of strings
lst=['Hello Everyone. ',
     '\nMy name is Josh Cullins. ',
     '\nI live in Texas. ',
     '\nTexas is an American State']

# Opening file in write mode
# 'w' mode creates a new file or overwrites existing content
with open('list.txt','w') as file:

    # writelines() writes list elements into file
    # It does not add separators automatically
    # Therefore '\n' is manually added inside strings where needed
    file.writelines(lst)
