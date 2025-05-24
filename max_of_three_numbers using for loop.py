list=[]

a = int(input("Enter how many numbers you want to check: "))
for i in range(a):
    num = int(input("Enter the number: "))
    list.append(num)

max = list[0]

for i in list:
    if i > max:
        max = i
print("Max number is: " + str(max))