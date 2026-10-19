# 6. If an employee ID exists, display the name.
# If it does not exist, add the employee ID and name.

employees = {
    101: "Aadil",
    102: "Rahul",
    103: "Aman"
}

emp_id = int(input("Enter employee ID: "))

if emp_id in employees:
    print("Employee name:", employees[emp_id])
else:
    name = input("Enter employee name: ")
    employees[emp_id] = name
    print("Employee added")

print(employees)