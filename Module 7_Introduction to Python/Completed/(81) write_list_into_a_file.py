# a Python program to write a list to a file

lst=['Hello Everyone. ','\nMy name is Josh Cullins. ','\nI live in Texas. ','\nTexas is an American State']
with open('list.txt','w') as file:

# writelines --- it writes a list of strings but with no separators. So we have to add sep in the strings provided
    file.writelines(lst)
