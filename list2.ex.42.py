# 42. Create a list of numbers divisible by both 3 and 5.

numbers = [number for number in range(1, 101) if number % 3 == 0 and number % 5 == 0]
print(numbers)