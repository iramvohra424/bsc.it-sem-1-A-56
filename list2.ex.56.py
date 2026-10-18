# 56. Accept a list and rotate it left and right by k positions.

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
k = int(input("Enter rotation positions: "))

if numbers:
    k = k % len(numbers)

    left = numbers[k:] + numbers[:k]
    right = numbers[-k:] + numbers[:-k] if k != 0 else numbers[:]

    print("Left rotation:", left)
    print("Right rotation:", right)
else:
    print("List is empty")