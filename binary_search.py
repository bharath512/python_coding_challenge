list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
num = int(input("Enter a number to search: "))
low = 0
high = len(list)-1

while low<=high:
    mid = (low + high) //2
    if list[mid] < num:
        low = mid + 1
    elif list[mid] > num:
        high= mid -1
    else:
        print(f"Number {list[mid]} is present")
        break