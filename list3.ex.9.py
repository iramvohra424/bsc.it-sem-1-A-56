# 9. When removing a student, remove all occurrences of the same name.

L1 = ["Aadil", "Rahul", "Aman", "Rahul", "Neha"]
name = input("Enter student name to remove: ")

while name in L1:
    L1.remove(name)

print(L1)