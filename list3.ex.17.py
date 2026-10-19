# 17. Separate odd and even numbers into two lists using list comprehension.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd = [n for n in numbers if n % 2 != 0]
even = [n for n in numbers if n % 2 == 0]

print("Odd numbers:", odd)
print("Even numbers:", even)