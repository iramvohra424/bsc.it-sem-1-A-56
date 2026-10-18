# 48. Store employee names, search for an employee, update the name if found, or add the name if not found.

employees = ["Amit", "Rahul", "Priya", "Neha"]

name = input("Enter employee name to search: ")

if name in employees:
    index = employees.index(name)
    new_name = input("Enter updated name: ")
    employees[index] = new_name
    print("Employee name updated")
else:
    employees.append(name)
    print("Employee added")

print(employees)