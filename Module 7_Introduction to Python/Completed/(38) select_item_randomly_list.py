# a Python program to select an item randomly from a list

# Importing random module
import random

# Loop will run 11 times
for i in range(11):
    lst_fruits=['Apple','Banana','Mango','Strawberry']

    # random.choice() selects a random item from the list
    print(random.choice(lst_fruits))