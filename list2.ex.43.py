# 43. Write a program to perform insertion, deletion, updating, sorting, reversing, and finding the highest, lowest, and average of list elements.

numbers = [10, 20, 30, 40, 50]

numbers.insert(2, 25)
print("After insertion:", numbers)

numbers.remove(30)
print("After deletion:", numbers)

numbers[0] = 15
print("After updating:", numbers)

numbers.sort()
print("Sorted list:", numbers)

numbers.reverse()
print("Reversed list:", numbers)

print("Highest:", max(numbers))
print("Lowest:", min(numbers))
print("Average:", sum(numbers) / len(numbers))