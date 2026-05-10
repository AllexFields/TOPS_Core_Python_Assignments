# a Python program to find the highest 3 values in a dictionary

my_dict={'a':1,'c':4,'d':13,'e':8,'b':2}
arranged_dict=dict(sorted(my_dict.items(),key=lambda i:i[1],reverse=True))
# print(arranged_dict)

emp_dict={}
count = 0

for k, v in arranged_dict.items():
    if count == 3:
        break
    emp_dict[k] = v
    count += 1

print(emp_dict)