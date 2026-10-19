# 10. Display the youngest student from the dictionary created above.

students = {
    "A": [20, "BCA", "Python"],
    "R": [19, "BSc", "Maths"],
    "N": [21, "BCom", "Accounts"]
}

youngest = min(students, key=lambda x: students[x][0])

print("Student initial:", youngest)
print("Age:", students[youngest][0])
print("Degree:", students[youngest][1])
print("Favourite subject:", students[youngest][2])