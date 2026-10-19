# 13. Create a nested employee list containing name, age, salary, and expertise.
# Ask for a name and display the employee details or an error message.

employees = [
    ["Aadil", 20, 25000, "Python"],
    ["Rahul", 22, 30000, "SQL"],
    ["Aman", 21, 28000, "Java"]
]

name = input("Enter employee name: ")
found = False

for emp in employees:
    if emp[0].lower() == name.lower():
        print("Name:", emp[0])
        print("Age:", emp[1])
        print("Salary:", emp[2])
        print("Expertise:", emp[3])
        found = True
        break

if not found:
    print("Employee not found")