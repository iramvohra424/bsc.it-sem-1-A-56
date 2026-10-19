# Exercise 2: Marks Lookup Without Error
# Search for DBMS and Networking using get(). Print "Subject not found"
# when a subject is missing. Print OS marks with default "Not Appeared"
# and display the dictionary to prove get() does not add a new key.

marks = {"Python": 78, "DBMS": 85, "Java": 69}

print("DBMS :", marks.get("DBMS", "Subject not found"))
print("Networking :", marks.get("Networking", "Subject not found"))
print("OS marks:", marks.get("OS", "Not Appeared"))
print(marks)