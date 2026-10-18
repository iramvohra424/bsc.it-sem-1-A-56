# 28. Find the first and last occurrence indices of an element in a list.

numbers = [10, 20, 30, 20, 40, 20]
element = int(input("Enter element: "))

if element in numbers:
    print("First occurrence:", numbers.index(element))
    print("Last occurrence:", len(numbers) - 1 - numbers[::-1].index(element))
else:
    print("Element not found")