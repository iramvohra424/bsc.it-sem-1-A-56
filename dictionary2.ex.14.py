# 14. Input roll numbers of 5 students and marks in 6 subjects,
# with each subject's marks out of 50. Store the minimum and maximum
# marks of each subject in separate dictionaries.

students = {}

for i in range(5):
    roll_no = int(input("Enter roll number: "))
    marks = input("Enter marks in 6 subjects separated by commas: ")
    students[roll_no] = [int(x.strip()) for x in marks.split(",")]

minimum_marks = {}
maximum_marks = {}

for subject in range(6):
    subject_marks = []

    for marks in students.values():
        subject_marks.append(marks[subject])

    minimum_marks[subject + 1] = min(subject_marks)
    maximum_marks[subject + 1] = max(subject_marks)

print("Minimum marks:", minimum_marks)
print("Maximum marks:", maximum_marks)