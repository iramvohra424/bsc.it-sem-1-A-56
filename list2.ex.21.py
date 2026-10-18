# 21. Rotate a list to the left and right by n positions.

numbers = [1, 2, 3, 4, 5]
n = int(input("Enter rotation positions: "))
n = n % len(numbers)

left = numbers[n:] + numbers[:n]
right = numbers[-n:] + numbers[:-n] if n != 0 else numbers[:]

print("Left rotation:", left)
print("Right rotation:", right)