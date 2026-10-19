# 13. Display the roll number of the student with the highest total marks.

students = {
    1: [78, 85, 69, 90, 82],
    2: [65, 72, 80, 75, 68],
    3: [90, 88, 95, 91, 87]
}

highest_roll = max(students, key=lambda roll: sum(students[roll]))

print("Roll number:", highest_roll)
print("Total marks:", sum(students[highest_roll]))