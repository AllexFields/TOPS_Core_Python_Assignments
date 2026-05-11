#  to check if a given key already exists in a dictionary

dictionary={"name":"Aastha",
            "age":23,
            "contact_no":9234920926,
            "city":"Delhi"
}

# Dictionary contains multiple keys:
# name, age, contact_no, and city

# Taking key input from the user
# .lower() converts input into lowercase for proper comparison
search_key=input("Enter key you want to search: ").lower()  
     
for i in dictionary.keys():
    if i==search_key:
        print(f"The key \'{search_key}\' is already present in given dictionary.")
        break

# This else block belongs to the for loop
# It executes only if loop completes without break statement
else:
    print(f"The key \'{search_key}\' is not present in given dictionary.")