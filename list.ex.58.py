# 58. find the smallest number using a loop

numbers = [25, 10, 45, 30, 15]

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print("Smallest number =", smallest)