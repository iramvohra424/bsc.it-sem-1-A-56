# 8. Remove the employee whose ID is provided by the user.

employees = {
    101: "Aadil",
    102: "Rahul",
    103: "Aman"
}

emp_id = int(input("Enter employee ID to remove: "))

if emp_id in employees:
    del employees[emp_id]
    print(employees)
else:
    print("Employee not found")