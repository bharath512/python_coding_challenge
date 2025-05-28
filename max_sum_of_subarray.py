list = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
current_sum = 0
max_sum = 0

for i in range(len(list)):
    if current_sum < 0:
        current_sum = 0
    current_sum = current_sum + list[i]
    if max_sum < current_sum:
        max_sum = current_sum

print(max_sum)