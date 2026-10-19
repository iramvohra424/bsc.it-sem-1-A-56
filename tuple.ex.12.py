# 12. Input a tuple and print its elements in reverse order.

items = input("Enter elements separated by commas: ").split(",")
t = tuple(items)

print("Original tuple:", t)
print("Reversed tuple:", t[::-1])