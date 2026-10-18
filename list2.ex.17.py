# 17. Split a list into chunks of size n.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = int(input("Enter chunk size: "))

if n > 0:
    for i in range(0, len(numbers), n):
        print(numbers[i:i + n])
else:
    print("Chunk size must be positive")