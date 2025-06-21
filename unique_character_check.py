s = input("Enter your string: ")

# With Built_in Function()
def is_unique_character_builtin(s):
    return len(set(s)) == len(s)

print(is_unique_character_builtin(s))

# Without Built_in Function()
def is_unique_character_notbuiltin(s):
    sum_c = 0
    for i in range(len(s)):
        for j in s:
            if s[i] == j:
                sum_c=sum_c+1
        if sum_c == 2:
            return False
        sum_c=0
    return True

print(is_unique_character_notbuiltin(s))

