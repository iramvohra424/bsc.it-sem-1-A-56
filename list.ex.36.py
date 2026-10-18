# 36. shopping cart program

cart = []

while True:
    print("1. Add item")
    print("2. Remove item")
    print("3. Display cart")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter item to add: ")
        cart.append(item)
        print("Item added")

    elif choice == 2:
        item = input("Enter item to remove: ")

        if item in cart:
            cart.remove(item)
            print("Item removed")
        else:
            print("Item not found")

    elif choice == 3:
        print("Shopping cart:", cart)

    elif choice == 4:
        break

    else:
        print("Invalid choice")