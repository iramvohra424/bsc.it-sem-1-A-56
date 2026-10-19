# 15. Find the maximum and minimum elements of a tuple without using max() or min().

numbers = (25, 10, 45, 5, 30)

maximum = numbers[0]
minimum = numbers[0]

for n in numbers:
    if n > maximum:
        maximum = n
    if n < minimum:
        minimum = n

print("Maximum:", maximum)
print("Minimum:", minimum)