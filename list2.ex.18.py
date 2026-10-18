# 18. Flatten a nested list into a single list.

nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = []

for sublist in nested_list:
    for number in sublist:
        flat_list.append(number)

print(flat_list)