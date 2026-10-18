# 54. Create two lists of equal size and create a third list containing the sums of corresponding elements.

list1 = [10, 20, 30, 40]
list2 = [1, 2, 3, 4]
result = []

for i in range(len(list1)):
    result.append(list1[i] + list2[i])

print("Sum list:", result)