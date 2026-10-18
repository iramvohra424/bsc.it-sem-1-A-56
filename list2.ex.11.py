# 11. Sort a list in ascending and descending order without using sort().

numbers = [40, 10, 30, 20, 50]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print("Ascending order:", numbers)
print("Descending order:", numbers[::-1])