# 11. If s2 is part of s1, print its first and last occurrences.

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if s2 in s1:
    print("First occurrence:", s1.find(s2))
    print("Last occurrence:", s1.rfind(s2))
else:
    print("s2 is not present in s1")