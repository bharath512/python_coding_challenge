list1 = [1, 2, 3, 4, 7, 9]
list2 = [9, 3, 4, 5, 6, 8]
common = []
for i in list1:
    for j in list2:
        if i == j:
           common.append(j)
print(list(dict.fromkeys(common)))