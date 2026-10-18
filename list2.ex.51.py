# 51. Create a menu-driven program to perform append, insert, extend, remove, pop, sort, reverse, count, index, copy, clear, and display operations on a list.

numbers = [10, 20, 30]

while True:
    print("\n1. Append")
    print("2. Insert")
    print("3. Extend")
    print("4. Remove")
    print("5. Pop")
    print("6. Sort")
    print("7. Reverse")
    print("8. Count")
    print("9. Index")
    print("10. Copy")
    print("11. Clear")
    print("12. Display")
    print("13. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        numbers.append(int(input("Enter number: ")))
    elif choice == "2":
        index = int(input("Enter index: "))
        value = int(input("Enter number: "))
        numbers.insert(index, value)
    elif choice == "3":
        values = list(map(int, input("Enter numbers separated by spaces: ").split()))
        numbers.extend(values)
    elif choice == "4":
        value = int(input("Enter number to remove: "))
        if value in numbers:
            numbers.remove(value)
        else:
            print("Number not found")
    elif choice == "5":
        if numbers:
            print("Removed:", numbers.pop())
        else:
            print("List is empty")
    elif choice == "6":
        numbers.sort()
    elif choice == "7":
        numbers.reverse()
    elif choice == "8":
        value = int(input("Enter number: "))
        print("Count:", numbers.count(value))
    elif choice == "9":
        value = int(input("Enter number: "))
        if value in numbers:
            print("Index:", numbers.index(value))
        else:
            print("Number not found")
    elif choice == "10":
        copied = numbers.copy()
        print("Copied list:", copied)
    elif choice == "11":
        numbers.clear()
    elif choice == "12":
        print(numbers)
    elif choice == "13":
        break
    else:
        print("Invalid choice")# 51. Create a menu-driven program to perform append, insert, extend, remove, pop, sort, reverse, count, index, copy, clear, and display operations on a list.

numbers = [10, 20, 30]

while True:
    print("\n1. Append")
    print("2. Insert")
    print("3. Extend")
    print("4. Remove")
    print("5. Pop")
    print("6. Sort")
    print("7. Reverse")
    print("8. Count")
    print("9. Index")
    print("10. Copy")
    print("11. Clear")
    print("12. Display")
    print("13. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        numbers.append(int(input("Enter number: ")))
    elif choice == "2":
        index = int(input("Enter index: "))
        value = int(input("Enter number: "))
        numbers.insert(index, value)
    elif choice == "3":
        values = list(map(int, input("Enter numbers separated by spaces: ").split()))
        numbers.extend(values)
    elif choice == "4":
        value = int(input("Enter number to remove: "))
        if value in numbers:
            numbers.remove(value)
        else:
            print("Number not found")
    elif choice == "5":
        if numbers:
            print("Removed:", numbers.pop())
        else:
            print("List is empty")
    elif choice == "6":
        numbers.sort()
    elif choice == "7":
        numbers.reverse()
    elif choice == "8":
        value = int(input("Enter number: "))
        print("Count:", numbers.count(value))
    elif choice == "9":
        value = int(input("Enter number: "))
        if value in numbers:
            print("Index:", numbers.index(value))
        else:
            print("Number not found")
    elif choice == "10":
        copied = numbers.copy()
        print("Copied list:", copied)
    elif choice == "11":
        numbers.clear()
    elif choice == "12":
        print(numbers)
    elif choice == "13":
        break
    else:
        print("Invalid choice")