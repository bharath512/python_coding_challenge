a = input("Enter a statment: ")
new_text=a.split()
word_count=[]

for i in new_text:
    word_count.append(len(i))

print(new_text[word_count.index(max(word_count))])