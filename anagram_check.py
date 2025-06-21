a = "listen"
b = "silent"

def is_anagram(a,b):
    if len(a)==len(b):
        for i in a:
            if i not in b:
                return False
        return True
    return False

print(is_anagram(a,b))
