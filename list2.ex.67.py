# 67. Create a menu-driven Student Record Management System to add, display, search, update, delete, sort students by name or marks, find the topper, and calculate the average marks.

students = []

while True:
    print("\n1. Add student")
    print("2. Display students")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Sort by name")
    print("7. Sort by marks")
    print("8. Find topper")
    print("9. Calculate average marks")
    print("10. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = input("Enter roll number: ")
        name = input("Enter student name: ")
        marks = float(input("Enter marks: "))
        students.append([roll, name, marks])
        print("Student added")

    elif choice == "2":
        if students:
            for student in students:
                print(student)
        else:
            print("No student records")

    elif choice == "3":
        roll = input("Enter roll number to search: ")
        found = False

        for student in students:
            if student[0] == roll:
                print(student)
                found = True
                break

        if not found:
            print("Student not found")

    elif choice == "4":
        roll = input("Enter roll number to update: ")
        found = False

        for student in students:
            if student[0] == roll:
                student[1] = input("Enter new name: ")
                student[2] = float(input("Enter new marks: "))
                print("Student updated")
                found = True
                break

        if not found:
            print("Student not found")

    elif choice == "5":
        roll = input("Enter roll number to delete: ")
        found = False

        for student in students:
            if student[0] == roll:
                students.remove(student)
                print("Student deleted")
                found = True
                break

        if not found:
            print("Student not found")

    elif choice == "6":
        students.sort(key=lambda student: student[1].lower())
        print("Students sorted by name")

    elif choice == "7":
        students.sort(key=lambda student: student[2], reverse=True)
        print("Students sorted by marks")

    elif choice == "8":
        if students:
            topper = max(students, key=lambda student: student[2])
            print("Topper:", topper)
        else:
            print("No student records")

    elif choice == "9":
        if students:
            average = sum(student[2] for student in students) / len(students)
            print("Average marks:", average)
        else:
            print("No student records")

    elif choice == "10":
        print("Exiting program")
        break

    else:
        print("Invalid choice")