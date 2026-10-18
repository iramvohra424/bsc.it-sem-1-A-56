# 62. Perform matrix addition, transpose, and calculate the sum of each row and column using nested lists.

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

addition = [
    [matrix1[i][j] + matrix2[i][j] for j in range(2)]
    for i in range(2)
]

transpose = [
    [matrix1[j][i] for j in range(2)]
    for i in range(2)
]

print("Matrix addition:")
for row in addition:
    print(row)

print("Transpose:")
for row in transpose:
    print(row)

for i, row in enumerate(matrix1):
    print("Sum of row", i + 1, "=", sum(row))

for j in range(2):
    column_sum = sum(matrix1[i][j] for i in range(2))
    print("Sum of column", j + 1, "=", column_sum)