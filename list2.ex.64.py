# 64. Create a frequency table for elements in a list.

numbers = [10, 20, 10, 30, 20, 10, 40]
frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

print("Element\tFrequency")
for number, count in frequency.items():
    print(number, "\t", count)