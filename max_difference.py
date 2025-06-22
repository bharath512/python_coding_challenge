lst = [2, 3, 10, 6, 4, 8, 1]

sum_diff=0
max_diff=0

for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i] < lst[j]:
            sum_diff=lst[j]-lst[i]
            if max_diff < sum_diff:
                max_diff=sum_diff
print(max_diff)
