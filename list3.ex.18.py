# 18. Create a mixed list of strings and integers.
# Print integer elements with and without list comprehension.

items = ["Python", 10, "SQL", 20, "Java", 30]

print("Without list comprehension:")
for item in items:
    if isinstance(item, int):
        print(item)

print("With list comprehension:")
numbers = [item for item in items if isinstance(item, int)]
print(numbers)