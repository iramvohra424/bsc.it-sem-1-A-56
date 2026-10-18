# 47. Accept 15 numbers, separate even and odd numbers, and display their count, sum, maximum, and minimum.

numbers = []

for i in range(15):
    number = int(input("Enter a number: "))
    numbers.append(number)

even = [number for number in numbers if number % 2 == 0]
odd = [number for number in numbers if number % 2 != 0]

print("Even numbers:", even)
print("Odd numbers:", odd)
print("Even count:", len(even))
print("Odd count:", len(odd))
print("Total sum:", sum(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))