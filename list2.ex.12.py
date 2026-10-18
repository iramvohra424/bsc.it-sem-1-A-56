# 12. Create a shallow copy of a list and show that changes to the copy do not affect the original list.

original = [10, 20, 30, 40]
copied = original.copy()

copied.append(50)

print("Original list:", original)
print("Copied list:", copied)