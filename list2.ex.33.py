# 33. Group elements in a list based on a condition.

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even = []
odd = []

for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print("Even numbers:", even)
print("Odd numbers:", odd)