# 60. Create a menu-driven program to add, display, search, update, and delete cities.

cities = []

while True:
    print("\n1. Add city")
    print("2. Display cities")
    print("3. Search city")
    print("4. Update city")
    print("5. Delete city")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        city = input("Enter city name: ")
        cities.append(city)
    elif choice == "2":
        print(cities)
    elif choice == "3":
        city = input("Enter city to search: ")
        print("Found" if city in cities else "Not found")
    elif choice == "4":
        city = input("Enter city to update: ")
        if city in cities:
            index = cities.index(city)
            cities[index] = input("Enter new city name: ")
        else:
            print("City not found")
    elif choice == "5":
        city = input("Enter city to delete: ")
        if city in cities:
            cities.remove(city)
        else:
            print("City not found")
    elif choice == "6":
        break
    else:
        print("Invalid choice")