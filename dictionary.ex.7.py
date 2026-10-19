# Exercise 7: Reverse Lookup (Name to Roll Number)
# Create a new dictionary where each student's name is the key and
# roll number is the value. Search for Bhavin and Zara using get().

rolls = {101: "Asha", 102: "Bhavin", 103: "Chirag"}
students = {}

for roll, name in rolls.items():
    students[name] = roll

print(students)
print("Roll of Bhavin:", students.get("Bhavin", "No such student"))
print("Roll of Zara :", students.get("Zara", "No such student"))