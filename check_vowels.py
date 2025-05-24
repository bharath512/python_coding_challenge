#! /usr/bin/env python

a = input("Enter a word to check vowels count: ")
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

def vowels_count(word):
    total_vowels = 0
    for i in word:
        for j in vowels:
            if i == j:
                total_vowels = total_vowels + 1
    print("Total Vowels: " + str(total_vowels))

vowels_count(a)
