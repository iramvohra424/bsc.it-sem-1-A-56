# Exercise 5: Word Frequency Counter
# Count how many times each word appears in the given sentence.
# Use get() with default 0. Do not use if-else to check whether
# a key exists in the dictionary.

sentence = "python is easy and python is powerful and python is popular"
words = sentence.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

for word, count in frequency.items():
    print(word, "->", count)