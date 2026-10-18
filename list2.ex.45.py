# 45. Create a menu-driven shopping list program to add, remove, search, update, sort, and display items.

shopping_list = []

while True:
    print("\n1. Add")
    print("2. Remove")
    print("3. Search")
    print("4. Update")
    print("5. Sort")
    print("6. Display")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item: ")
        shopping_list.append(item)
    elif choice == "2":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            print("Item not found")
    elif choice == "3":
        item = input("Enter item to search: ")
        print("Found" if item in shopping_list else "Not found")
    elif choice == "4":
        old_item = input("Enter item to update: ")
        if old_item in shopping_list:
            index = shopping_list.index(old_item)
            shopping_list[index] = input("Enter new item: ")
        else:
            print("Item not found")
    elif choice == "5":
        shopping_list.sort()
        print("List sorted")
    elif choice == "6":
        print(shopping_list)
    elif choice == "7":
        break
    else:
        print("Invalid choice")