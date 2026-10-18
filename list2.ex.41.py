# 41. Generate a multiplication table as a list of lists using list comprehension.

table = [[number * i for i in range(1, 11)] for number in range(1, 11)]

for row in table:
    print(row)