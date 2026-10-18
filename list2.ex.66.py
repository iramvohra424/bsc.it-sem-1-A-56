# 66. Convert a list of marks into grades A, B, C, D, or F using list comprehension.

marks = [95, 82, 73, 65, 40, 25]

grades = [
    "A" if mark >= 90 else
    "B" if mark >= 80 else
    "C" if mark >= 70 else
    "D" if mark >= 40 else
    "F"
    for mark in marks
]

print("Marks:", marks)
print("Grades:", grades)