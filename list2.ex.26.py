# 26. Swap two elements at given positions in a list.

numbers = [10, 20, 30, 40, 50]
i = int(input("Enter first index: "))
j = int(input("Enter second index: "))

numbers[i], numbers[j] = numbers[j], numbers[i]
print(numbers)