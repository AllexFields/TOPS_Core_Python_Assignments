# Count the occurrences of each word in a sentence

sentence=input("Enter a sentence: ")

# Splitting sentence into separate words using space as separator
words=sentence.split(" ")

# Creating an empty list to store already counted words
lst=[]

for i in words:

    if i not in lst:
        print(f"\"{i}\" occurs {words.count(i)} times")
        lst.append(i)


    