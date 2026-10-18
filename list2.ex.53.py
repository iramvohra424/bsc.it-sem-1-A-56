# 53. Create a list of 20 numbers and remove all prime numbers.

numbers = list(range(1, 21))
result = []

for number in numbers:
    is_prime = number > 1

    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break

    if not is_prime:
        result.append(number)

print("List without prime numbers:", result)