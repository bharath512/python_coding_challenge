s = input("Enter your string: ")

# With built-in function
def reverse_string_builtin(s):
    print(s[::-1])

reverse_string_builtin(s)

# Without built-in function
def reverse_string_not_builtin(s):
    new_string=""
    for i in range(len(s)):
        new_string = new_string + s[-i-1]
    print(new_string)

reverse_string_not_builtin(s)
