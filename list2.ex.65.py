# 65. Use list comprehension to create squares, cubes, even numbers, odd numbers, and multiples of 5 from 1 to 100.

squares = [number ** 2 for number in range(1, 101)]
cubes = [number ** 3 for number in range(1, 101)]
even = [number for number in range(1, 101) if number % 2 == 0]
odd = [number for number in range(1, 101) if number % 2 != 0]
multiples_of_5 = [number for number in range(1, 101) if number % 5 == 0]

print("Squares:", squares)
print("Cubes:", cubes)
print("Even numbers:", even)
print("Odd numbers:", odd)
print("Multiples of 5:", multiples_of_5)