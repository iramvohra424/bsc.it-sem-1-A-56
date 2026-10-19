# Exercise 1: Library Book Record
# Given a book dictionary, print all keys, all values, each key-value pair,
# and the total number of fields using keys(), values(), and items().

book = {
    "id": "B101",
    "title": "Python Basics",
    "author": "R. Mehta",
    "copies": 3
}

print("Keys     :", list(book.keys()))
print("Values :", list(book.values()))

for key, value in book.items():
    print(key, ":", value)

print("Total fields:", len(book))