# 7. Change the employee name for the employee ID entered by the user.

employees = {
    101: "Aadil",
    102: "Rahul",
    103: "Aman"
}

emp_id = int(input("Enter employee ID: "))

if emp_id in employees:
    name = input("Enter new employee name: ")
    employees[emp_id] = name
    print(employees)
else:
    print("Employee not found")