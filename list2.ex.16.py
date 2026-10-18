# 16. Find the second-largest and second-smallest elements in a list.

numbers = [10, 20, 30, 40, 50]
unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

unique_numbers.sort()

if len(unique_numbers) >= 2:
    print("Second smallest:", unique_numbers[1])
    print("Second largest:", unique_numbers[-2])
else:
    print("Not enough distinct elements")