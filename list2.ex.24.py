# 24. Separate even and odd numbers in a list.

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