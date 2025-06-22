from collections import Counter

s = input("Enter your string: ")

# With built-in function
def char_frequency_builtin(s):
    return dict(Counter(s))

print(char_frequency_builtin(s))

# Without built-in function
def char_frequency_notbuiltin(s):
    freq={}
    for i in s:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    print(freq)

char_frequency_notbuiltin(s)
