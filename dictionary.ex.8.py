# Exercise 8: Merge Two Divisions' Results
# Merge both divisions into a new dictionary using update().
# Remove absent students using pop(), find the topper using an items()
# loop without max(), and print students with marks >= 60.

div_a = {"Asha": 72, "Bhavin": 64, "Chirag": 88}
div_b = {"Dhruv": 59, "Bhavin": 70, "Esha": 91}
absent = ["Chirag"]

combined = div_a.copy()
combined.update(div_b)

print("Combined:", combined)

for name in absent:
    combined.pop(name, None)

print("After removing absentees:", combined)

topper_name = ""
topper_marks = -1

for name, marks in combined.items():
    if marks > topper_marks:
        topper_name = name
        topper_marks = marks

print("Topper:", topper_name, topper_marks)

passed = []

for name, marks in combined.items():
    if marks >= 60:
        passed.append(name)

print("Passed:", passed)