a = int(input("Enter a number: "))
num = 1
for i in range(a,0,-1):
    num = num*i
print(f"Factorial of {a} is {num}")