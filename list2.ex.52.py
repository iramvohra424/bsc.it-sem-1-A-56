# 52. Accept a list and display the first five elements, last five elements, alternate elements, and reversed list using slicing.

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("First five:", numbers[:5])
print("Last five:", numbers[-5:])
print("Alternate elements:", numbers[::2])
print("Reversed list:", numbers[::-1])