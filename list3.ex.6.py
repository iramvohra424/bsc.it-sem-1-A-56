# 6. If a student is present, display the count of the same name
# and the position of its first occurrence.

L1 = ["Aadil", "Rahul", "Aman", "Rahul", "Neha"]
name = input("Enter student name: ")

if name in L1:
    print("Count:", L1.count(name))
    print("First position:", L1.index(name))
else:
    print("Student not found")