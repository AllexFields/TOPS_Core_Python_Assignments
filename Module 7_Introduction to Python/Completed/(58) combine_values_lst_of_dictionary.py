# Python program to combine values in a list of dictionaries

'''
Sample Data = [ {'item': 'item1', 'amount': 400},
            {'item': 'item2', 'amount': 300},
            {'item': 'item1', 'amount': 750}
]

Expected Output:
{'item1': 1150, 'item2': 300}
'''

lst=[{'item': 'item1', 'amount': 400},{'item': 'item2', 'amount': 300},{'item': 'item1', 'amount': 750}] 

# Creating an empty dictionary to store final result
emp_dic={}

for i in lst:
    # Extracting item name
    item_name = i['item']

    # Extracting item amount
    item_amount = i['amount']

    # Checking whether item already exists in emp_dic    
    if item_name not in emp_dic:

        # If item is not present, add item with its amount
        emp_dic[item_name]=item_amount

    else:
        # If item already exists, add current amount
        # to existing amount value
        emp_dic[item_name]+=item_amount


print(emp_dic)



