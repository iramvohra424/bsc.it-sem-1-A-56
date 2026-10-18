# 44. find the position of a student's name

students = ["Aman", "Rahul", "Priya", "Aadil", "Neha"]

name = input("Enter student name: ")

if name in students:
    print("Position:", students.index(name) + 1)
else:
    print("Student not found")