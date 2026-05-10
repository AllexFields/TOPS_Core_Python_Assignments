'''a Python program to combine values in python list of dictionaries.
 
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 
300}, o {'item': 'item1', 'amount': 750}] 
Expected Output: 
Counter ({'item1': 1150, 'item2': 300})''' 

lst=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300},{'item': 'item1', 'amount': 750}] 

emp_dic={}
for i in lst:
    item_name = i['item']
    item_amount = i['amount']

# Check if 'item1' or 'item2' is present in emp_dic, if present then it simply adds the value of 'amount' key
# else if not present it adds the 'item' with 'amount'    
    if item_name not in emp_dic:
        emp_dic[item_name]=item_amount
    else:
        emp_dic[item_name]+=item_amount

print(emp_dic)



