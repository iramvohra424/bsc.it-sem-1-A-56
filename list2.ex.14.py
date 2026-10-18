# 14. Convert a list of strings into a list of integers.

numbers = ["10", "20", "30", "40", "50"]
integer_list = []

for number in numbers:
    integer_list.append(int(number))

print(integer_list)