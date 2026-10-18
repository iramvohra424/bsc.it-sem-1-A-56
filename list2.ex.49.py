# 49. Convert a sentence into words, count each word's occurrence, and remove repeated words.

sentence = input("Enter a sentence: ")
words = sentence.split()
frequency = {}
unique_words = []

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
        unique_words.append(word)

print("Word frequency:", frequency)
print("Words without repetition:", unique_words)