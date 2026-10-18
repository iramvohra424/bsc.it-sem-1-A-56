# 38. Generate a list of prime numbers up to 100 using list comprehension.

primes = [
    number for number in range(2, 101)
    if all(number % divisor != 0 for divisor in range(2, int(number ** 0.5) + 1))
]

print(primes)