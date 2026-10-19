# 5. Input an employee ID and check whether the employee exists.

employees = {
    101: "Aadil",
    102: "Rahul",
    103: "Aman"
}

emp_id = int(input("Enter employee ID: "))

if emp_id in employees:
    print("Employee exists")
else:
    print("Employee does not exist")