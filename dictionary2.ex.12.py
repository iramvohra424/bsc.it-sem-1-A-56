# 12. Create a dictionary using the above marks dictionary.
# Use roll number as key and (total, percentage, grade) as a tuple.

students = {
    1: [78, 85, 69, 90, 82],
    2: [65, 72, 80, 75, 68],
    3: [90, 88, 95, 91, 87]
}

result = {}

for roll_no, marks in students.items():
    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 35:
        grade = "D"
    else:
        grade = "Fail"

    result[roll_no] = (total, percentage, grade)

print(result)