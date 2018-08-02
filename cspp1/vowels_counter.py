"'vowels'"
VOWEL = input("Enter a string")
VOWELS = 0
CONSONANTS = 0
for i in VOWEL:
    if i in 'aeiou':
        VOWELS = VOWELS + 1
    else:
        CONSONANTS = CONSONANTS + 1

print("Number of vowels:")
print(str(VOWELS))
