# 37. Flatten a two-dimensional list using nested list comprehension.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [number for row in matrix for number in row]

print(flat_list)