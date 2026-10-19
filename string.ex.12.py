# 12. If s2 is present in s1, count the number of times it occurs.

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if s2 in s1:
    print("Occurrences:", s1.count(s2))
else:
    print("s2 is not present in s1")