# 55. Find the longest string, shortest string, strings starting with a vowel, and strings ending with a consonant.

words = ["apple", "banana", "orange", "grapes", "kiwi"]

if words:
    print("Longest string:", max(words, key=len))
    print("Shortest string:", min(words, key=len))

vowel_start = [word for word in words if word[0].lower() in "aeiou"]
consonant_end = [
    word for word in words
    if word[-1].isalpha() and word[-1].lower() not in "aeiou"
]

print("Strings starting with a vowel:", vowel_start)
print("Strings ending with a consonant:", consonant_end)