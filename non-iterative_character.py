a = input("Enter a string to find first non-iterative character: ")
new_text=a.lower()

for i in range(len(new_text)):
    new_str=new_text[:i]+new_text[i+1:]
    if new_text[i] not in new_str:
        print(f"First non-iterative character in your word is '{a[i]}'")
        break
