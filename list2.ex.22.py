# 22. Remove all occurrences of a given element from a list.

numbers = [10, 20, 10, 30, 10, 40]
element = int(input("Enter element to remove: "))

result = []

for number in numbers:
    if number != element:
        result.append(number)

print(result)