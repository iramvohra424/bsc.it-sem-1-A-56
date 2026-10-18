# 32. Find the longest consecutive sequence in a list.

numbers = [100, 4, 200, 1, 3, 2]
numbers = sorted(set(numbers))

longest = []
current = []

for number in numbers:
    if not current or number == current[-1] + 1:
        current.append(number)
    else:
        if len(current) > len(longest):
            longest = current
        current = [number]

if len(current) > len(longest):
    longest = current

print("Longest consecutive sequence:", longest)