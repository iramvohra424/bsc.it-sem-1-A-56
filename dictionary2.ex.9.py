# 9. Input 5 student names and create a dictionary with initials as keys
# and a list containing age, degree, and favourite subject as values.

students = {}

for i in range(5):
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    degree = input("Enter degree: ")
    subject = input("Enter favourite subject: ")

    initial = name[0].upper()
    students[initial] = [age, degree, subject]

print(students)