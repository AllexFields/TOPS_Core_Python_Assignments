#  to check if a given key already exists in a dictionary

dictionary={"name":"Aastha","age":23,"contact_no":9234920926,"city":"Delhi"}
# there are multiple keys --- name,age,contact_no & city --- in our dictionary
# Now we have to check whether a given key is already present in our dictionary or not

search_key=input("Enter key you want to search: ").lower()      # because all our keys are in lower case 
for i in dictionary.keys():
    if i==search_key:
        print(f"The key \'{search_key}\' is already present in given dictionary.")
        break
else:
    print(f"The key \'{search_key}\' is not present in given dictionary.")