# 16. Create a list of 10 numbers and find the total of odd numbers
# and the total of even numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_total = 0
even_total = 0

for n in numbers:
    if n % 2 == 0:
        even_total += n
    else:
        odd_total += n

print("Odd total:", odd_total)
print("Even total:", even_total)