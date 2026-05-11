# a Python program to unzip a list of tuples into individual lists



a=[(1, 'astha'), (2, 'shivam'), (3, 'vyom'), (4, 'sandeep'), (45, 'anjali')]

# Unzipping list of tuples
# *a unpacks all tuples into separate arguments
# zip() groups first elements together and second elements together
lst,lst1=zip(*a)         
     
# Converting tuples into lists and printing them
print(list(lst),list(lst1))