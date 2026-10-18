# 46. Merge two lists, remove duplicates, and sort in ascending and descending order.

list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

merged = list1 + list2
unique = []

for number in merged:
    if number not in unique:
        unique.append(number)

unique.sort()
print("Ascending order:", unique)
print("Descending order:", unique[::-1])