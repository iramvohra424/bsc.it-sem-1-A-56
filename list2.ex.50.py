# 50. Store student details in a nested list, find the topper, and sort students by marks.

students = [
    [1, "Amit", 85],
    [2, "Rahul", 92],
    [3, "Priya", 78],
    [4, "Neha", 95]
]

topper = max(students, key=lambda student: student[2])
print("Topper:", topper)

students.sort(key=lambda student: student[2], reverse=True)

print("Students sorted by marks:")
for student in students:
    print(student)