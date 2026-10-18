# 35. Filter vowels from a list of characters using list comprehension.

characters = ['a', 'b', 'e', 'f', 'i', 'k', 'o', 'u']
vowels = [char for char in characters if char.lower() in "aeiou"]

print(vowels)