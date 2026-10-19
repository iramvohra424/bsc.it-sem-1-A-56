# Exercise 6: Stationery Shop Stock
# Process each order using get(). Reject orders when the quantity exceeds
# available stock. Remove items with zero stock using pop(). Finally,
# restock stapler and notebook using one update() call.

stock = {"pen": 10, "notebook": 4, "eraser": 2}
orders = [("pen", 3), ("eraser", 2), ("stapler", 1), ("notebook", 5)]

for item, quantity in orders:
    available = stock.get(item)

    if available is None:
        print(item + ": not available")
    elif quantity > available:
        print(item + ": only " + str(available) + " left, order rejected")
    else:
        stock[item] = available - quantity
        print(item + ": sold " + str(quantity))

        if stock[item] == 0:
            stock.pop(item)
            print(item + ": out of stock, removed")

stock.update({"stapler": 5, "notebook": 10})
print("Stock after restock:", stock)