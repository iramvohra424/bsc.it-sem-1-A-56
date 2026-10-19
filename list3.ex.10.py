# 10. Create a list of 10 numbers and find the maximum and minimum.

numbers = []

for i in range(10):
    n = int(input("Enter a number: "))
    numbers.append(n)

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))