# 40. Extract words longer than five characters from a sentence using list comprehension.

sentence = input("Enter a sentence: ")
words = sentence.split()

result = [word for word in words if len(word) > 5]
print(result)