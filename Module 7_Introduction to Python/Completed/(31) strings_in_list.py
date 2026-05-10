#  to count the number of strings where the string length is 2 or more 
# and the first and last character are same from a given list of strings

lst_string=['Kenyk','Cuba','Brazil','Chinc','Somalia']
count=0
for i in lst_string:
    i=i.lower()       # to make all letters of i either be small or capital...to compare 1st & last letters
    if len(i)>=2 and i[0]==i[-1]:
        count+=1
print(f"there are {count} no of such strings in given list")
