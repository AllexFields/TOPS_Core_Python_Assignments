'''To randomize items of a list we can use shuffle method of random module.....
To randomize or shuffle the items of a list in place in Python, we use the shuffle() method 
of the random module.
The shuffle() method changes the original order of elements directly inside the same list.'''

import random
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)