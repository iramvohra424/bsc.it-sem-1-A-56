# Exercise 4: College Canteen Menu
# Print item names using dictionary iteration, print the price list using
# items(), calculate total and average prices using a loop on values()
# without sum(), and print items priced above Rs. 30.

menu = {
    "Tea": 15,
    "Coffee": 25,
    "Samosa": 20,
    "Sandwich": 60,
    "Cold Coffee": 70
}

print("Items:")
for item in menu:
    print("  ", item)

print("Price list:")
for item, price in menu.items():
    print("  ", item, "Rs.", price)

total = 0

for price in menu.values():
    total += price

average = total / len(menu)
print("Total of all items:", total)
print("Average price      :", average)

expensive = []

for item, price in menu.items():
    if price > 30:
        expensive.append(item)

print("Items above Rs. 30:", expensive)