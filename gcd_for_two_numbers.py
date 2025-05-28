a = int(input("Enter number for first input: "))
b = int(input("Enter number for Second input: "))
max = 0

for i in range(1,10001,1):
    if a%i==0 and b%i==0:
        if i>max:
            max = i

print(max)