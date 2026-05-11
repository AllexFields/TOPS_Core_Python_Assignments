# To get the largest number, smallest num and sum of all from a list.

lst=[12,233,45,-18,94]
sum=0

# Sorting list in ascending order
# By default, sort() arranges elements from smallest to largest
lst.sort()

# Printing smallest element
print(f"Smallest no. is {lst[0]}")

# Printing largest element
print(f"Largest no. is {lst[-1]}")

for i in lst:
    sum+=i
print(f"Sum of all elements in {lst} : {sum}")


# Or we can use max & min function to get smallest and largest number

# print(f"Smallest no. is {min(lst)}")
# print(f"Largest no. is {max(lst)}")

