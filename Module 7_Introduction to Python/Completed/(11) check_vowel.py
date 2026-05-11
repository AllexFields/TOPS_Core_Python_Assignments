# whether a passed letter is a vowel or not

letter=input("Enter a letter: ")


# Checking if the entered letter is present in vowel characters
if letter in "a,e,i,o,u":
    print(f"{letter} is a vowel")
    
else: print(f"{letter} is not a vowel")