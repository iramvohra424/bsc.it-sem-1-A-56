# 7. Count the occurrences of an element in a list.

numbers = [10, 20, 10, 30, 10, 40]
element = 10
count = 0

for number in numbers:
    if number == element:
        count += 1

print("Occurrences =", count)