# 8. Remove a particular student name entered by the user.

L1 = ["Aadil", "Rahul", "Aman", "Priya", "Neha"]
name = input("Enter student name to remove: ")

if name in L1:
    L1.remove(name)
    print(L1)
else:
    print("Student not found")