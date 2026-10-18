# 30. Interleave two lists.

list1 = [1, 3, 5]
list2 = [2, 4, 6]
result = []

for i in range(min(len(list1), len(list2))):
    result.append(list1[i])
    result.append(list2[i])

result.extend(list1[len(list2):])
result.extend(list2[len(list1):])

print(result)