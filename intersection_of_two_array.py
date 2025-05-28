a = {1, 2, 3}
b = {2, 3, 4}

new_list=[]

for i in a:
    for j in b:
        if i ==j:
            new_list.append(i)

print(new_list)

#====================================================
# Using pre defined function
a = {1, 2, 3}
b = {2, 3, 4}

print(a & b)