# 15. Input 6 fruits and store each fruit's buying and selling price
# in a tuple. Display fruits with profit, loss, and no profit/loss.

fruits = {}

for i in range(6):
    name = input("Enter fruit name: ")
    buying = float(input("Enter buying price: "))
    selling = float(input("Enter selling price: "))

    fruits[name] = (buying, selling)

print("Profit:")
for fruit, prices in fruits.items():
    if prices[0] < prices[1]:
        print(fruit)

print("Loss:")
for fruit, prices in fruits.items():
    if prices[0] > prices[1]:
        print(fruit)

print("No profit or loss:")
for fruit, prices in fruits.items():
    if prices[0] == prices[1]:
        print(fruit)