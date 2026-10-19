# 11. Create a tuple of 10 integers and separate odd and even numbers into two tuples.

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

odd = ()
even = ()

for n in numbers:
    if n % 2 == 0:
        even += (n,)
    else:
        odd += (n,)

print("Odd numbers:", odd)
print("Even numbers:", even)