# a Python program to find the highest 3 values in a dictionary

my_dict={'a':1,'c':4,'d':13,'e':8,'b':2}

# Sorting dictionary in descending order based on values
# reverse=True sorts values from highest to lowest
arranged_dict=dict(sorted(my_dict.items(),key=lambda i:i[1],reverse=True))

# Creating an empty dictionary to store top 3 values
emp_dict={}

# Initializing the counter variable
count = 0

for k, v in arranged_dict.items():

    # Stopping loop after storing 3 items
    if count == 3:
        break

    # Adding key-value pair into new dictionary
    emp_dict[k] = v

    # Increasing counter value
    count += 1

print(emp_dict)