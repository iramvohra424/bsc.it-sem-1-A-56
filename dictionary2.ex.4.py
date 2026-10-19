# 4. Display all employee names and create a separate list of names.

employees = {
    101: "Aadil",
    102: "Rahul",
    103: "Aman"
}

names = list(employees.values())

print("Employee names:", employees.values())
print("Name list:", names)