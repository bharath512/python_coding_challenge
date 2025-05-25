import string

list = string.ascii_uppercase

a = input("Enter a word to check: ")
count = 0
for i in a:
    for j in list:
        if i == j:
            count = count + 1

print(count)
