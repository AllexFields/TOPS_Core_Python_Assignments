# Program to count the number of strings where:
# 1. String length is 2 or more
# 2. First and last characters are the same


lst_string=['Kenyk','Cuba','Brazil','Chinc','Somalia']
count=0
for i in lst_string:
    # Converting string into lowercase
    # This helps in case-insensitive comparison
    i=i.lower()

    if len(i)>=2 and i[0]==i[-1]:
        count+=1
        
print(f"there are {count} no of such strings in given list")
