# 9. Create a menu-driven program to find string length, convert to uppercase,
# convert to lowercase, capitalize the initial letter, and split the string.

s = input("Enter a string: ")

print("1. Length")
print("2. Uppercase")
print("3. Lowercase")
print("4. Capitalize")
print("5. Split")

choice = int(input("Enter your choice: "))

if choice == 1:
    print(len(s))
elif choice == 2:
    print(s.upper())
elif choice == 3:
    print(s.lower())
elif choice == 4:
    print(s.capitalize())
elif choice == 5:
    print(s.split())
else:
    print("Invalid choice")