# 8. Check whether an element exists in a list.

numbers = [10, 20, 30, 40, 50]
element = int(input("Enter a number to search: "))

if element in numbers:
    print("Element found")
else:
    print("Element not found")