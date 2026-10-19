# 6. Create a tuple of 5 fruits, take a fruit name as input, and search for it.

fruits = ("Apple", "Mango", "Banana", "Orange", "Grapes")
fruit = input("Enter a fruit name: ")

if fruit in fruits:
    print("Fruit found")
else:
    print("Fruit not found")