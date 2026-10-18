# 58. Replace all negative numbers in a list with zero.

numbers = [10, -5, 20, -8, 30, -2]

for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = 0

print(numbers)