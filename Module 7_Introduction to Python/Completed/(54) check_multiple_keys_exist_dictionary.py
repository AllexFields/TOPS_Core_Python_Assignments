# a Python program to check multiple keys exists in a dictionary 

main_dictionary={
    "name":"Shivam",
    "age":21,
    "status":"Single",
    "job":"Data Analyst"
}

# we need to check whether these keys(multiple keys) exist in our dictionary or not

required_keys=["name","age","gender"]

for k in required_keys:
    if k in main_dictionary.keys():
        print(f"'{k}' exists as key in dictionary")
    else:
        print(f"'{k}' doesn't exist as key in dictionary")