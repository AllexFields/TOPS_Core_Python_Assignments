# Count the occurrences of each word in a sentence

sentence=input("Enter a sentence: ")
words=sentence.split(" ")
lst=[]
for i in words:
    if i not in lst:
        print(f"\"{i}\" occurs {words.count(i)} times")
        lst.append(i)


    