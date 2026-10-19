# 11. Create a list of alphabets and count the vowels.

alphabets = ['a', 'b', 'e', 'f', 'i', 'k', 'o', 'u']
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0

for ch in alphabets:
    if ch.lower() in vowels:
        count += 1

print("Total vowels:", count)