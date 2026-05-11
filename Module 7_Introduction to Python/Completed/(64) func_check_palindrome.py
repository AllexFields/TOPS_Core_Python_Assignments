#  A Python function that checks whether a passed string is palindrome or not 

# Defining function to check palindrome
def check_palindrome(name):

    # Reversing the string using slicing
    # -1::-1 starts from last character and moves backward
    new_string=name[-1::-1]

    # Comparing original string with reversed string
    if new_string==name:
        print(f"{name} is palindrome")
    
    # If both strings are not equal
    else:
        print(f"{name} is not palindrome")


string_input=input("Enter a string: ")
check_palindrome(string_input)

    




    

















# if its a palindrome ---> 121 reverse is 121,mam reverse is mam

# num=1323
# temp=num
# rev=0
# while num>0:
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10
# if rev==temp:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")
