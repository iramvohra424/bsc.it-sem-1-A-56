# 63. Find missing numbers between the minimum and maximum values in a list.

numbers = [1, 2, 4, 6, 7, 10]
missing = []

for number in range(min(numbers), max(numbers) + 1):
    if number not in numbers:
        missing.append(number)

print("Missing numbers:", missing)