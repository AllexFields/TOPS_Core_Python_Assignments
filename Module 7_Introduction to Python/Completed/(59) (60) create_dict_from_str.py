# A Python program to create a dictionary from a string
# string:'w3resource' 
# Expected output: • {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

string='aastha123'
dictionary={}
for i in string:
    dictionary[i]=string.count(i)
print(dictionary)