s = input("Enter your string: ")

# With built-in function
def sum_of_digit_builtin(s):
    total=0
    for i in s:
        if i.isdigit():
            total=total+int(i)
    print(total)
sum_of_digit_builtin(s)

# Without built-in function
def sum_of_digit_notbuiltin(s):
    total = 0
    for i in s:
        for j in range(0,10):
            if i == str(j):
                total = total + int(i)
    print(total)

sum_of_digit_notbuiltin(s)
