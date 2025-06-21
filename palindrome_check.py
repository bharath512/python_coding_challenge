s = input("Enter your string: ")

# With Built_in Function()
def is_palindrome_builtin(s):
    return s.lower() == s.lower()[::-1]

print(is_palindrome_builtin(s))

# Without Built_in Function()
def is_palindrome_not_builtin(s):
    count = len(s)//2
    for i in range(count):
        if s.lower()[i] == s.lower()[-i-1]:
            return True
        else:
            return False
print(is_palindrome_not_builtin(s))
