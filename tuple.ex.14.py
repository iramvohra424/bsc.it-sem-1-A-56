# 14. Take a string as input and count total vowels using a tuple of vowels.

s = input("Enter a string: ").lower()
vowels = ('a', 'e', 'i', 'o', 'u')
count = 0

for ch in s:
    if ch in vowels:
        count += 1

print("Total vowels:", count)