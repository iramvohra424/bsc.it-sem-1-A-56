# 57. Find the second-largest and second-smallest elements without using built-in sorting.

numbers = [10, 40, 20, 50, 30]
unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)

if len(unique) >= 2:
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if unique[i] > unique[j]:
                unique[i], unique[j] = unique[j], unique[i]

    print("Second smallest:", unique[1])
    print("Second largest:", unique[-2])
else:
    print("Not enough distinct elements")